from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('article/', views.article_list),
    path('article/<int:article_pk>/', views.article_detail),

    path('article/<int:article_pk>/comment/', views.comment_create),  # 댓글 생성 (POST)
    path('article/comment/<int:comment_pk>/', views.comment_detail),  # 댓글 수정 (PUT), 삭제 (DELETE)
]
