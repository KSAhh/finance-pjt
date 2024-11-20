from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('save/', views.save_products),      # 상품 데이터 저장

    path('', views.product_list),                               # 전체 상품 조회
    path('<int:product_pk>/', views.product_detail),            # 단일 상품 조회

    # path('product-options/<str:fin_prdt_cd>/', views.product_options), # 옵션 조회
    # path('top-rate/', views.top_rate), # 최고우대금리상품 조회
]
