import requests

from django.shortcuts import get_list_or_404, get_object_or_404
from django.conf import settings
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


from .models import Product, ProductOption
from .serializers import ProductSerializer, ProductOptionSerializer

FSS_API_KEY = settings.FSS_API_KEY
BASE_URL = "http://finlife.fss.or.kr/finlifeapi/"


# 정기예금 상품, 옵션목록 DB에 저장
@api_view(['GET'])
@permission_classes([IsAdminUser])  # 관리자만 접근 가능
def save_products(request, product_type):

    # API에서 데이터 가져오기
    URL = f"{BASE_URL}{product_type}ProductsSearch.json"
    params = {
        'auth': FSS_API_KEY,
        'topFinGrpNo': '020000', # 금융회사 코드 - 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    result = response.get("result", {})

    # API 응답 실패 - 오류 반환
    if result.get("err_cd", {}) != "000":
        detail = result.get("err_msg", "Invalid API request.")
        return Response({"detail" : detail}, status=status.HTTP_400_BAD_REQUEST)
    
    # API 응답 성공 - 상품, 옵션 데이터 가져오기
    product_list = result.get('baseList', [])   # 상품목록
    option_list = result.get('optionList', [])  # 옵션목록

    for product_data in product_list:
        # 중복 상품 검사 (금융상품 코드 기준)
        if Product.objects.filter(fin_prdt_cd=product_data.get('fin_prdt_cd')).exists():
            continue
        
        # 상품 저장
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid(raise_exception=True):
            product = product_serializer.save() # 상품 객체 반환

        # 옵션 저장
        if ProductOption.objects.filter(product=product).exists(): 
            continue
        
        for option_data in option_list:
            if option_data.get('fin_prdt_cd') == product_data.get('fin_prdt_cd'):
                option_serializer = ProductOptionSerializer(data=option_data)
                if option_serializer.is_valid(raise_exception=True):
                    option_serializer.save(product=product)
    return Response({'detail': 'Successfully saved.'}, status=status.HTTP_201_CREATED)


# 전체 상품 목록 조회 (GET)
@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = get_list_or_404(Product)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    # 상품 데이터 저장 (POST)
    # if request.method == 'POST':
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response({'detail' : "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
# 단일 상품 조회 (GET)
@api_view(['GET'])
def product_detail(request, product_pk):
    print("product pk:     ", product_pk)
    if request.method == "GET":
        product = get_object_or_404(Product, pk=product_pk)
        options = ProductOption.objects.filter(product=product)
        
        product_serializer = ProductSerializer(product)
        options_serializer = ProductOptionSerializer(options, many=True)
        return Response({"product": product_serializer.data, "options": options_serializer.data}, status=status.HTTP_200_OK)

# 특정 상품의 옵션 리스트 출력
# @api_view(['GET'])
# def product_options(request, fin_prdt_cd):
#     options = get_list_or_404(ProductOption, fin_prdt_cd=fin_prdt_cd)
#     serializer = ProductOptionSerializer(options, many=True)
#     return Response(serializer.data)


# 최고 우대 금리의 상품, 옵션 리스트 출력
# @api_view(['GET'])
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
