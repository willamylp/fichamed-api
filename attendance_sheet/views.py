from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from app.permissions import GlobalDefaultPermission
from medical_history.models import MedicalCareHistory
from .models import AttendanceSheet
from .serializers import AttendanceSheetSerializer, AttendanceSheetDetailSerializer, AttendanceSheetPanelSerializer


class AttendanceSheetListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = AttendanceSheet.objects.all()
    serializer_class = AttendanceSheetSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        "card_number",
        "patient_name",
        "classification",
    ]
    filterset_fields = [
        "card_number",
        "patient_name",
        "classification",
    ]
    ordering = ["id"]

    def perform_create(self, serializer):
        serializer.save(filled_by=self.request.user)


class AttendanceSheetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = AttendanceSheet.objects.all()
    serializer_class = AttendanceSheetDetailSerializer

    def perform_update(self, serializer):
        serializer.save(filled_by=self.request.user)


class MedicalCareSheetPanelListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = AttendanceSheet.objects.exclude(
        id__in=MedicalCareHistory.objects.values('attendance_sheet')
    ).values(
        "id",
        "card_number",
        "patient_name",
        "classification",
        'created_at',
    )
    serializer_class = AttendanceSheetPanelSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        "card_number",
        "patient_name",
        "classification",
    ]
    filterset_fields = [
        "card_number",
        "patient_name",
        "classification",
    ]
    ordering = ["id"]
