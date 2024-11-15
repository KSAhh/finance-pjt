from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


# 고객센터 전체 글 조회(GET) & 작성(POST)
@api_view(["GET", "POST"])
def article_list(request):
    if request.method == "GET":
        # articles = Article.objects.filter(is_delete=False)  # 소프트 삭제 제외
        articles = get_list_or_404(Article.objects.filter(is_delete=False))
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({ "message" : "Successfully created." }, status=status.HTTP_201_CREATED)
            

# 고객센터 단일 글 조회(GET) & 수정(PUT) & 삭제(DELETE)
@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk, is_delete=False)
    article = get_object_or_404(Article.objects.filter(is_delete=False), pk=article_pk)
    # comments = get_list_or_404(Comment.objects.filter(is_delete=False), article=article) 
    comments = Comment.objects.filter(article=article, is_delte=False)

    if request.method == "GET":
        article_serializer = ArticleSerializer(article)
        comments_serializer = CommentSerializer(comments, many=True) # 댓글목록 쿼리셋 직렬화
        serializer = {
            "article" : article_serializer.data,
            "comments" : comments_serializer.data,
        }
        return Response(serializer)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            # return Response(serializer.data)
            return Response({ "message" : "Successfully updated."}, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        comments.update(is_delete=True)
        article.is_delete = True
        article.save()
        return Response({ "message" : "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT)

    
# 댓글 생성(POST)
@api_view(["POST"])
def comment_create(request, article_pk):
    article = get_object_or_404(Article.objects.filter(is_delete=False), pk=article_pk)
    
    serializer = CommentSerializer(data=request.data)   # 댓글 쿼리셋을 직렬화
    if serializer.is_valid(raise_exception=True):       
        serializer.save(article=article) # 유효성 검사 목록에서 article 제외
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({ "message" : "Successfully created."}, status=status.HTTP_201_CREATED)


# 댓글 수정(PUT) & 삭제(DELETE)
@api_view(["PUT", "DELETE"])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment.objects.filter(is_delete=False), pk=comment_pk)
    
    # if request.method == "GET":
    #     serializer = CommentSerializer(comment)                     # 댓글 쿼리셋을 직렬화
    #     return Response(serializer.data)
    if request.method == "DELETE":
        comment.is_delete = True
        comment.save()
        # comment.delete()                                            # 댓글 쿼리셋을 삭제
        return Response({ "message" : "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data, partial=True)  # 댓글 쿼리셋을 직렬화
        if serializer.is_valid(raise_exception=True):
            serializer.save(commenter=request.user)
            # return Response(serializer.data)
            return Response({ "message" : "Successfully updated."}, status=status.HTTP_200_OK)