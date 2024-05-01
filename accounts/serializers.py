from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
            "created_at": {
                "read_only": True
            },
            "updated_at": {
                "read_only": True
            },
            "last_login": {
                "read_only": True
            },
        }
