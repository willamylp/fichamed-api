from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.hashers import make_password
from app.permissions import GlobalDefaultPermission
from .models import User
from .serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        "full_name", "username", "email",
        "created_at", "updated_at"
    ]
    filterset_fields = [
        "full_name", "username",
        "created_at", "updated_at"
    ]
    ordering = ["id"]

    def perform_create(self, serializer):
        serializer.save(
            password=make_password(
                serializer.validated_data['password']
            )
        )


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
