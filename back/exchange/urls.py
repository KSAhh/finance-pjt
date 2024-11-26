from django.urls import path
from . import views

app_name="exchange"

urlpatterns = [
    path("", views.rate_list), # 환율조회
    path("save-exchange/", views.save_exchange) # 환율 데이터 저장
]
