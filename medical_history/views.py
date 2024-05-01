from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from app.permissions import GlobalDefaultPermission
from .models import MedicalCareHistory
from .serializers import MedicalCareHistorySerializer


class MedicalCareHistoryListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = MedicalCareHistory.objects.all()
    serializer_class = MedicalCareHistorySerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        "attendance_sheet",
        "doctor_attended",
        "service_date",
    ]
    filterset_fields = [
        "attendance_sheet",
        "doctor_attended",
        "service_date"
    ]
    ordering = ["id"]



class MedicalCareHistoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = MedicalCareHistory.objects.all()
    serializer_class = MedicalCareHistorySerializer
