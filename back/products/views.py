import requests
from django.shortcuts import get_list_or_404
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer

# Create your views here.

FSS_API_KEY = settings.FSS_API_KEY
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

# 정기예금 상품 목록, 옵션목록 DB에 저장
@api_view(['GET'])
def save_deposit_products(request):
    print(FSS_API_KEY)

    # API에서 데이터 가져오기
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth': FSS_API_KEY,
        # 금융회사 코드
        # - 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    if response.get("result", {}).get("err_cd", {}) != "000" : # API 응답실패
        print("여기1  ",response)
        detail = response.get("result", {}).get("err_msg","Invalid API request.")
        return Response({"detail" : detail}, status=status.HTTP_400_BAD_REQUEST)
    print("여기2  ",response)
    product_list = response.get('result', {}).get('baseList', [])   # 상품목록
    option_list = response.get('result', {}).get('optionList', [])  # 옵션목록
    for product_data in product_list:
        # 금융상품 코드가 존재하지 않는 경우, 상품 저장
        if DepositProducts.objects.filter(fin_prdt_cd=product_data.get('fin_prdt_cd')).exists():
            continue

        product_serializer = DepositProductsSerializer(data=product_data)
        if product_serializer.is_valid(raise_exception=True):
            product = product_serializer.save() # 상품 객체 반환

        # 금융상품 코드가 동일한 옵션이 없는 경우, 옵션 저장
        if DepositOptions.objects.filter(product=product).exists(): 
            continue
        
        for option_data in option_list:
            if option_data.get('fin_prdt_cd') == product_data.get('fin_prdt_cd'):
                option_serializer = DepositOptionsSerializer(data=option_data)
                if option_serializer.is_valid(raise_exception=True):
                    option_serializer.save(product=product)
    return Response({'detail': 'Successfully saved.'}, status=status.HTTP_201_CREATED)


# GET: 전체 정기예금 상품 목록 출력
# POST: 상품 데이터 저장
@api_view(['GET', 'POST'])
def deposit_products(request):
    products = get_list_or_404(DepositProducts)
    if request.method == 'GET':
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        context = {
            'message' : "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
        

# 특정 상품의 옵션 리스트 출력
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = get_list_or_404(DepositOptions, fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)

# 가입 기간에 상관없이 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력 
@api_view(['GET'])
def top_rate(request):
    options = get_list_or_404(DepositOptions)
    max_rate = -1       # 가장 높은 최고 우대금리
    top_product = None   # 최고 우대금리 옵션
    for option in options:
        if option.intr_rate2 and option.intr_rate2 > max_rate:
            max_rate = option.intr_rate2
            top_product = option.product
    # 최고 우대금리 상품이 없는 경우
    if top_product is None:
        return Response({"message" : "최고 우대금리를 확인할 수 있는 옵션이 없습니다."}, status=status.HTTP_404_NOT_FOUND)    
    
    # 최고 우대금리 옵션을 가진 상품, 옵션 정보 반환
    product_serializer = DepositProductsSerializer(top_product)
    options_serializer = DepositOptionsSerializer(DepositOptions.objects.filter(product=top_product), many=True)
    return Response({
        "deposit_product" : product_serializer.data,
        "options": options_serializer.data
        }, status=status.HTTP_200_OK)
