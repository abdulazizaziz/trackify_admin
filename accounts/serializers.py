from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as BaseTokenSerializer,
)
from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer,
)
from django.contrib.auth.models import update_last_login
from .models import *

class TokenSerializer(BaseTokenSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["superadmin"] = user.is_superuser
        token["email"] = user.email
        update_last_login(None, user)
        return token


class CreateUserSerializer(BaseUserCreateSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "password",
        ]