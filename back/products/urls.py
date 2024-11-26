from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('', views.product_list),                       # 전체 상품 조회 
    path('save-products/', views.save_products),                 # 상품 데이터 저장
    path('<int:product_pk>/<str:product_type>/', views.product_detail),    # 단일 상품 조회
    
    path('user/', views.user_product_list), # 유저 상품 전체 조회, 생성
    path('user/<int:product_pk>/', views.user_product_detail),   # 유저 상품 단일 조회, 수정, 삭제 

    # path('product-options/<str:fin_prdt_cd>/', views.product_options), # 옵션 조회
    path('top-rate/', views.top_rate), # 최고우대금리상품 조회

]
