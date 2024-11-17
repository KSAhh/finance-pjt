from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "fullname", "nickname"]

    def create(self, validated_data):
        # UserManager의 create_user 메서드 호출
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            fullname=validated_data["fullname"],
            nickname=validated_data["nickname"],
        )
        return user
