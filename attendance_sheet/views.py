from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from app.permissions import GlobalDefaultPermission
from .models import AttendanceSheet
from .serializers import AttendanceSheetSerializer


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


class AttendanceSheetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = AttendanceSheet.objects.all()
    serializer_class = AttendanceSheetSerializer
