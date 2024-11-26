from rest_framework import serializers
from .models import Article, Comment


# 글
class ArticleSerializer(serializers.ModelSerializer):
    author_nickname = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']

    def get_author_nickname(self, obj):
        # author가 존재하면 nickname 반환, 없으면 None
        return obj.author.nickname if obj.author else None
    

# 댓글
class CommentSerializer(serializers.ModelSerializer):
    
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ['title'] # article의 title만 전달
    article = ArticleTitleSerializer(read_only=True)
    commenter_nickname = serializers.SerializerMethodField()  # 댓글 작성자의 닉네임 추가

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'commenter']
    
    def get_commenter_nickname(self, obj):
        # commenter가 존재하면 nickname 반환, 없으면 None
        return obj.commenter.nickname if obj.commenter else None
