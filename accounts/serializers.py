from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username", "password",
            "full_name", "email",
            "groups", "user_permissions",
            "is_active", "is_staff", "is_superuser"
        ]
