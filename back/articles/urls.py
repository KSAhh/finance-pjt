from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.article_list),                               # 글 생성
    path('<int:article_pk>/', views.article_detail),            # 글 조회, 수정, 삭제

    path('<int:article_pk>/comment/', views.comment_create),    # 댓글 생성
    path('comment/<int:comment_pk>/', views.comment_detail),    # 댓글 수정, 삭제
]
