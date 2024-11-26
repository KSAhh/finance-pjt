import requests

from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response

# permission Decorators
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from .models import DepositProduct, SavingProduct, ProductOption, UserProduct
from .serializers import DepositSavingSerializer, ProductOptionSerializer, UserProductSerializer, DepositSavingDetailSerializer, ProductRecommendSeriazlier

from django.contrib.contenttypes.models import ContentType

from datetime import date, datetime

FSS_API_KEY = settings.FSS_API_KEY
BASE_URL = "http://finlife.fss.or.kr/finlifeapi/"
KAKAO_API_KEY = settings.KAKAO_API_KEY
KAKAO_JS_KEY = settings.KAKAO_JS_KEY

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
                
                if PRODUCT_TYPES == "deposit" and TOP_FIN_GRP_NO_LIST == "020000":
                    print(result)
                    
                # API 응답 성공 - 상품, 옵션 데이터 가져오기
                product_list = result.get("baseList", [])   # 상품목록
                option_list = result.get("optionList", [])  # 옵션목록

                # 상품 객체 생성
                for product_data in product_list:

                    # 중복 상품 검사
                    model_class = DepositProduct if product_type == "deposit" else SavingProduct
                    if model_class.objects.filter(
                        kor_co_nm=product_data.get("kor_co_nm"),
                        fin_prdt_cd=product_data.get("fin_prdt_cd")
                    ).exists():
                        print("중복상품 : ", product_data)
                        continue

                    # max_limit, join_way 필드 값이 None, 빈 문자열 등일 경우 기본값 설정
                    max_limit = product_data.get("max_limit", -1.00)
                    if max_limit in [None, ""]:
                        max_limit = -1.00

                    # join_way 전처리 (리스트로 변환)
                    join_way_data = product_data.get("join_way", "Unknown")
                    if join_way_data in [None, ""]:
                        join_way_data = "Unknown"
                    join_way_list = [way.strip() for way in join_way_data.split(",")] # 문자열로 들어 온 여러 개의 데이터를 나눠서 저장

                    
                    # 상품 저장
                    product_data_common = { # 상품 공통 필드
                        "kor_co_nm" : product_data.get("kor_co_nm", "Unknown"),
                        "fin_prdt_cd" : product_data.get("fin_prdt_cd", "Unknown"),
                        "fin_prdt_nm" : product_data.get("fin_prdt_nm", "Unknown"),
                        "join_way" : join_way_list,
                        "mtrt_int" : product_data.get("mtrt_int", "Unknown"),
                        "spcl_cnd" : product_data.get("spcl_cnd", "Unknown"),
                        "join_deny" : product_data.get("join_deny", 1),
                        "join_member" : product_data.get("join_member", "실명의 개인"),
                        "etc_note" : product_data.get("etc_note", "Unknown"),
                        "fin_co_subm_day" : product_data.get("fin_co_subm_day", "000000000000"),
                        "max_limit" : max_limit
                    }
                    product = model_class.objects.create(**product_data_common)                           
                    
                    # 옵션 저장
                    for option in option_list:
                        # 금융상품 코드가 동일하면 옵션 저장
                        if option.get("fin_prdt_cd") != product.fin_prdt_cd:
                            continue

                        # `intr_rate` 값 검증 및 기본값 설정
                        intr_rate = option.get("intr_rate", 0.00)
                        if intr_rate in [None, ""]:
                            intr_rate = 0.00

                        # 옵션 객체 생성 및 저장
                        ProductOption.objects.create(
                            # GenericForeignKey 필드 설정
                            content_type=ContentType.objects.get_for_model(product),
                            object_id=product.id,

                            # 기존
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
        deposit_products = DepositProduct.objects.prefetch_related("options").all()
        saving_products = SavingProduct.objects.prefetch_related("options").all()
        if deposit_products or saving_products:
            deposit_serializer = DepositSavingDetailSerializer(deposit_products, many=True)
            saving_serializer = DepositSavingDetailSerializer(saving_products, many=True)
            
            detail = {
                "deposits" : deposit_serializer.data,
                "savings": saving_serializer.data,
            }
            return Response(detail, status=status.HTTP_200_OK)
        return Response({"detail" : "조회 가능한 상품이 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    # 상품 데이터 저장 (POST)
    # if request.method == "POST":
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response({"detail" : "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
# 단일 상품 조회 (GET)
@api_view(["GET"])
def product_detail(request, product_pk, product_type):

    if request.method == "GET":
        """
        특정 금융상품의 옵션 데이터 조회
        :param product_type: 상품 유형 ("deposit" 또는 "saving")
        :param product_id: 금융상품 ID
        """
        # Product 모델 설정
        product_model = ""
        if product_type == "deposit":
            product_model = DepositProduct
        elif product_type == "saving":
            product_model = SavingProduct
        else:
            return Response({"detail": "product type은 deposit 또는 saving이여야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        # 금융상품 조회
        product = get_object_or_404(product_model, pk=product_pk)

        # 관련 옵션 데이터 조회
        options = product.options.all() # 역참조

        product_serializer = DepositSavingSerializer(product)
        options_serializer = ProductOptionSerializer(options, many=True) # 데이터 직렬화
        
        detail = {
            "product" : product_serializer.data,
            "options" : options_serializer.data,
        }
        return Response(detail, status=status.HTTP_200_OK)

# 특정 상품의 옵션 리스트 출력
# @api_view(["GET"])
# def product_options(request, fin_prdt_cd):
#     options = get_list_or_404(ProductOption, fin_prdt_cd=fin_prdt_cd)
#     serializer = ProductOptionSerializer(options, many=True)
#     return Response(serializer.data)


# 최고 우대 금리의 상품, 옵션 리스트 출력
@api_view(["GET"])
def top_rate(request):
    """
    DepositProduct와 SavingProduct 각각의 최고 우대금리(top rate) 기준 상위 5개의 옵션 반환.
    """
    # DepositProduct와 SavingProduct의 content_type 가져오기
    deposit_content_type = ContentType.objects.get_for_model(DepositProduct)
    saving_content_type = ContentType.objects.get_for_model(SavingProduct)


    # DepositProduct 관련 옵션
    deposit_options = (
        ProductOption.objects.filter(content_type=deposit_content_type)
        .order_by("-intr_rate")[:10]
    )

    # SavingProduct 관련 옵션
    saving_options = (
        ProductOption.objects.filter(content_type=saving_content_type)
        .order_by("-intr_rate")[:10]
    )

    # 직렬화
    deposit_serializer = ProductRecommendSeriazlier(deposit_options, many=True)
    saving_serializer = ProductRecommendSeriazlier(saving_options, many=True)

    return Response(
        {
            "deposit_top_rates": deposit_serializer.data,
            "saving_top_rates": saving_serializer.data,
        },
        status=status.HTTP_200_OK,
    )

# @api_view(["GET"])
# def top_rate(request):
#     options = get_list_or_404(ProductOption)
#     print(options)
#     top_option = max(options, key=lambda x: x.intr_rate2 or 0)
#     top_product = top_option.product

#     # 최고 우대금리 옵션을 가진 상품, 옵션 정보 반환
#     product_serializer = ProductOptionSerializer(top_product)
#     options_serializer = ProductOptionSerializer(top_option)
#     return Response({
#         "products" : product_serializer.data,
#         "options": options_serializer.data
#         }, status=status.HTTP_200_OK)

# 유저 상품 전체 조회 (GET)
# 유저 상품 생성 (POST)
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated]) 
def user_product_list(request):
    if request.method == "GET":
        products = get_list_or_404(UserProduct, user=request.user)
        serializer = UserProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        """
        유저가 가입한 금융상품 저장.
        """
        product_data = request.data
        product_type = product_data.get("product_type")
        product_pk = product_data.get("product_pk") 
        deposit_product = None
        saving_product = None

        # DB내 상품과 연동
        if product_pk != None:
            if product_type == "예금" or product_type == "deposit":
                deposit_product = DepositProduct.objects.filter(pk=product_pk).first()
            elif product_type == "적금" or product_type == "saving":
                saving_product = SavingProduct.objects.filter(pk=product_pk).first()
            elif product_type != "기타":
                return Response({"detail" : "지원가능한 타입의 상품이 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        # 동일 은행, 같은 상품인 경우 저장하지 않음
        fin_prdt_nm = product_data.get("fin_prdt_nm")
        kor_co_nm = product_data.get("kor_co_nm")
        if UserProduct.objects.filter(fin_prdt_nm=fin_prdt_nm, kor_co_nm=kor_co_nm).exists():
            return Response({"detail": "동일한 상품이 이미 등록되어있습니다."}, status=status.HTTP_400_BAD_REQUEST)

        # 잔액이 음수인 경우 저장하지 않음
        if int(product_data.get("balance", 0)) < 0: 
            return Response({"detail" : "balance 값은 0이상이어야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserProductSerializer(data=product_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, deposit_product=deposit_product, saving_product=saving_product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 유저 상품 단일 조회 (GET)
# 유저 상품 수정 (PUT)
# 유저 상품 삭제 (DELETE)
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def user_product_detail(request, product_pk):
    product = get_object_or_404(UserProduct, pk=product_pk)
    
    # 유저 본인 상품만 확인 가능
    if product.user.id != request.user.id: 
        return Response({"detail": "접근 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == "GET":
        serializer = UserProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":

        # 상품의 타입에 따라 수정 가능한 필드를 제한
        product_type = product.product_type
        data = request.data

        # 연동된 상품이 있는 경우, 데이터 일부 변경만 가능
        if product.deposit_product or product.saving_product:
            if 'kor_co_nm' in data or 'fin_prdt_nm' in data or 'product_type' in data:
                return Response({"detail": "연동된 상품이 있어 금융기관과 상품명을 변경할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        # 지정된 타입만 저장
        print(data.get("product_type"), "?")
        if data.get("product_type", product_type) not in ["예금", "deposit", "적금", "saving", "기타", "etc", ""]:
            return Response({"detail" : "지원가능한 타입(예금, 적금, 기타)의 상품이 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        
        # 날짜제한
        # 시작일 : 미래일 지정 불가
        start_date = data.get("start_date", product.start_date)

        # 현재 날짜 확인
        # 문자열인 경우만 datetime.date로 변환
        try:
            if isinstance(start_date, str):
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        except ValueError as e:
            return Response({"detail": "날짜 형식(%Y-%m-%d)이 맞지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
        if start_date > date.today():
            return Response({"detail" : "start_date는 오늘보다 미래를 지정할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "DELETE":
        product.delete()
        product.save()
        return Response({"detail" : "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
