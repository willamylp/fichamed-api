from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from .models import MedicalCareHistory
from .serializers import MedicalCareHistorySerializer


class MedicalCareHistoryListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = MedicalCareHistory.objects.all()
    serializer_class = MedicalCareHistorySerializer


class MedicalCareHistoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = MedicalCareHistory.objects.all()
    serializer_class = MedicalCareHistorySerializer
