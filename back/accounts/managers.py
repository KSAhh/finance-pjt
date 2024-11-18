from django.contrib.auth.models import BaseUserManager

# 유저생성 커스텀
class UserManager(BaseUserManager):
    def create_user(self, username, password, fullname, nickname=None, email=None, profile_image='profile_images/default.png', **extra_fields):
        """
        일반 유저 생성
        """
        if not username:
            raise ValueError("The Username must be set")
        if not password:
            raise ValueError("The Password must be set")
        if not fullname:
            raise ValueError("The Fullname must be set")
        # 이메일 정규화
        email = self.normalize_email(email) if email else None 
        # 유저 생성
        user = self.model(username=username, password=password, fullname=fullname, nickname=nickname, email=email, profile_image=profile_image, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        슈퍼 유저 생성
        """        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # 필요한 필드에 기본값 추가
        extra_fields.setdefault('nickname', 'Admin')
        extra_fields.setdefault('fullname', 'superuser')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, email, password, **extra_fields)