from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from .models import AttendanceSheet
from .serializers import AttendanceSheetSerializer


class AttendanceSheetListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = AttendanceSheet.objects.all()
    serializer_class = AttendanceSheetSerializer


class AttendanceSheetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = AttendanceSheet.objects.all()
    serializer_class = AttendanceSheetSerializer
