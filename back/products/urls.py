from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('', views.product_list),                       # 전체 상품 조회
    path('save/', views.save_products),                 # 상품 데이터 저장
    path('user-products/<int:user_pk>/', views.user_products, name="user_products"), # 유저 상품 등록, 조회

    path('<str:product_type>/<int:product_pk>/', views.product_detail, name="product_detail"),    # 단일 상품 조회
    # path('product-options/<str:fin_prdt_cd>/', views.product_options), # 옵션 조회
    # path('top-rate/', views.top_rate), # 최고우대금리상품 조회

]
