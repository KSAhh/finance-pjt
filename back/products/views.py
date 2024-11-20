import requests

from django.shortcuts import get_list_or_404, get_object_or_404
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response

# permission Decorators
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAdminUser


from .models import Product, JoinWay, ProductOption, Bank, BankProduct
from .serializers import ProductSerializer, ProductOptionSerializer

FSS_API_KEY = settings.FSS_API_KEY
BASE_URL = "http://finlife.fss.or.kr/finlifeapi/"


# 정기예금 상품, 옵션목록 DB에 저장
@api_view(["GET"])
@permission_classes([IsAdminUser])  # 관리자만 접근 가능
def save_products(request):
    # API에서 데이터 가져오기
    PRODUCT_TYPES = ["deposit", "saving"]  # 상품 유형
    TOP_FIN_GRP_NO_LIST = ["020000", "030300"]  # 금융회사 코드 목록
    MAX_PAGE_NO = {
        "deposit": {"020000": 1, "030300": 4},
        "saving": {"020000": 1, "030300": 3},
    }  # 각 상품 유형 및 금융회사별 페이지 수

    for product_type in PRODUCT_TYPES:  # deposit, saving
        for top_fin_grp_no in TOP_FIN_GRP_NO_LIST:
            max_page_no = MAX_PAGE_NO[product_type].get(top_fin_grp_no, 1)
            for page_no in range(1, max_page_no + 1):
                URL = f"{BASE_URL}{product_type}ProductsSearch.json"
                params = {
                    "auth": FSS_API_KEY,
                    "topFinGrpNo": top_fin_grp_no,
                    "pageNo": page_no,
                }
                response = requests.get(URL, params=params).json()
                result = response.get("result", {})

                # API 응답 실패 - 오류 반환
                if result.get("err_cd", {}) != "000":
                    print(f"Failed for {product_type}, topFinGrpNo={top_fin_grp_no}, pageNo={page_no}")
                    continue
            
                # API 응답 성공 - 상품, 옵션 데이터 가져오기
                product_list = result.get("baseList", [])   # 상품목록
                option_list = result.get("optionList", [])  # 옵션목록

                # 상품 객체 생성
                for product_data in product_list:
                    # 중복 상품 검사
                    if Product.objects.filter(
                        kor_co_nm=product_data.get("kor_co_nm"),
                        fin_prdt_cd=product_data.get("fin_prdt_cd"),
                    ).exists():
                        print(product_data)
                        continue

                    # max_limit, join_way 필드 값이 None, 빈 문자열 등일 경우 기본값 설정
                    max_limit = product_data.get("max_limit", -1.00)
                    if max_limit in [None, ""]:
                        max_limit = -1.00
                    
                    # 상품 저장 (기본값 DB에서 지정)
                    product = Product.objects.create(
                        kor_co_nm=product_data.get("kor_co_nm", "Unknown"),
                        fin_prdt_cd=product_data.get("fin_prdt_cd", "Unknown"),
                        fin_prdt_nm=product_data.get("fin_prdt_nm", "Unknown"),
                        mtrt_int=product_data.get("mtrt_int", "Unknown"),
                        spcl_cnd=product_data.get("spcl_cnd", "Unknown"),
                        join_deny=product_data.get("join_deny", 1),
                        join_member=product_data.get("join_member", "실명의 개인"),
                        etc_note=product_data.get("etc_note", "Unknown"),
                        fin_co_subm_day=product_data.get("fin_co_subm_day", "000000000000"),
                        max_limit=max_limit,
                    )

                    # join_way 데이터 제1정규화 처리
                    join_way_data = product_data.get("join_way", "Unknown")
                    if join_way_data in [None, ""]:
                        join_way_data = "Unknown"
                    join_way_list = [way.strip() for way in join_way_data.split(",")] # 문자열로 들어 온 여러 개의 데이터를 나눠서 저장

                    for way in join_way_list:
                        JoinWay.objects.create(product=product, way=way)

                    for option in option_list:

                        # 금융상품 코드가 동일하지 않으면 건너뜀
                        if option.get("fin_prdt_cd") != product.fin_prdt_cd:
                            continue

                        # `intr_rate` 값 검증 및 기본값 설정
                        intr_rate = option.get("intr_rate", -1.00)
                        if intr_rate in [None, ""]:
                            intr_rate = -1.00

                        # 옵션 객체 생성 및 저장 -------------------------------------------------------- 여러번의 INSERT 발생 -> 오버헤드
                        ProductOption.objects.create(
                            product=product,
                            intr_rate_type_nm=option.get("intr_rate_type_nm", "Unknown"),
                            save_trm=option.get("save_trm", -1),
                            intr_rate=intr_rate,
                            intr_rate2=option.get("intr_rate2", -1.00),
                            rsrv_type_nm=option.get("rsrv_type_nm", 0.00),
                        )

    return Response({"detail": "Successfully saved."}, status=status.HTTP_201_CREATED)


# 전체 상품 목록 조회 (GET)
@api_view(["GET"])
def product_list(request):
    if request.method == "GET":
        products = get_list_or_404(Product)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    # 상품 데이터 저장 (POST)
    # if request.method == "POST":
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response({"detail" : "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
# 단일 상품 조회 (GET)
@api_view(["GET"])
def product_detail(request, product_pk):
    print("product pk:     ", product_pk)
    if request.method == "GET":
        product = get_object_or_404(Product, pk=product_pk)
        options = ProductOption.objects.filter(product=product)
        
        product_serializer = ProductSerializer(product)
        options_serializer = ProductOptionSerializer(options, many=True)
        return Response({"product": product_serializer.data, "options": options_serializer.data}, status=status.HTTP_200_OK)

# 특정 상품의 옵션 리스트 출력
# @api_view(["GET"])
# def product_options(request, fin_prdt_cd):
#     options = get_list_or_404(ProductOption, fin_prdt_cd=fin_prdt_cd)
#     serializer = ProductOptionSerializer(options, many=True)
#     return Response(serializer.data)


# 최고 우대 금리의 상품, 옵션 리스트 출력
# @api_view(["GET"])
# def top_rate(request):
#     options = get_list_or_404(ProductOption)
    
#     top_option = max(options, key=lambda x: x.intr_rate2 or 0)
#     top_product = top_option.product

#     # 최고 우대금리 옵션을 가진 상품, 옵션 정보 반환
#     product_serializer = ProductSerializer(top_product)
#     options_serializer = ProductOptionSerializer(top_option)
#     return Response({
#         "deposit_product" : product_serializer.data,
#         "options": options_serializer.data
#         }, status=status.HTTP_200_OK)




@api_view(["GET"])
@permission_classes([IsAdminUser])  # 관리자만 접근 가능
def save_bank_info(request, bank_name):
    KAKAO_API_KEY = settings.KAKAO_API_KEY
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {
        "query": bank_name,
        "size": 15,  # 최대 15개의 결과
    }

    # API 호출
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return Response(
            {"detail": "Failed to fetch data from Kakao API"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    # 결과 처리
    result = response.json()
    places = result.get("documents", [])
    if not places:
        return Response(
            {"detail": f"No bank information found for {bank_name}"},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    # 은행 정보 저장
    for place in places:
        Bank.objects.update_or_create(
            bank_name=place.get("place_name", "Unknown"),
            address=place.get("road_address_name", place.get("address_name", "Unknown")),
            defaults={
                "latitude": float(place.get("y", 0.0000)),
                "longitude": float(place.get("x", 0.0000)),
            },
        )

    return Response(
        {"detail": f"Bank information for {bank_name} has been saved."},
        status=status.HTTP_200_OK,
    )
