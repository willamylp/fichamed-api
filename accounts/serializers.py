from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username", "password",
            "full_name", "email",
            "groups", "user_permissions",
            "is_active", "is_staff", "is_superuser",
            "created_at", "updated_at"
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "created_at": {
                "read_only": True
            },
            "updated_at": {
                "read_only": True
            }
        }

