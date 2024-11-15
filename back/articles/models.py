from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  # AUTH_USER_MODEL 참조

# 고객센터 글
# 필수 - title, article_body
# 자동 - created_at, updated_at
# 관계 - author_id
class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)       # 글 제목
    article_body = models.TextField(null=False, blank=False)                # 글 본문
    image = models.ImageField(upload_to='images/', blank=True, null=True)   # 이미지 파일 경로
    is_private = models.BooleanField(default=False)                         # 글 비공개 여부
    is_delete = models.BooleanField(default=False)                          # 글 삭제여부 / 소프트 삭제
    created_at = models.DateTimeField(auto_now_add=True)                    # 글 작성 일시
    updated_at = models.DateTimeField(auto_now=True)                        # 글 수정 일시
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='articles') # 글 작성자

    def __str__(self):
        return f'"{self.title}"'


# 고객센터 댓글
# 필수 - comment_body
# 자동 - created_at, updated_at
# 관계 - article_id, commenter_id
class Comment(models.Model):
    comment_body = models.TextField(null=False, blank=False)    # 댓글 본문
    is_delete = models.BooleanField(default=False)              # 댓글 삭제여부 / 소프트 삭제
    created_at = models.DateTimeField(auto_now_add=True)        # 댓글 작성 일시
    updated_at = models.DateTimeField(auto_now=True)            # 댓글 수정 일시

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments') # 댓글 단 글
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='comments') # 댓글 작성자

    def __str__(self):
        return f'"{self.article}" 글의 댓글'
        # return f'"{self.article}" 글에 대한 {self.user}의 댓글"'
