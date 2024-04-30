from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from accounts.serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


