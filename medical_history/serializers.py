from rest_framework import serializers
from accounts.serializers import UserSerializer
from attendance_sheet.serializers import AttendanceSheetSerializer
from attendance_sheet.models import AttendanceSheet
from .models import MedicalCareHistory


class MedicalCareHistorySerializer(serializers.ModelSerializer):

    attendance_sheet = serializers.PrimaryKeyRelatedField(
        queryset=AttendanceSheet.objects.exclude(
            id__in=MedicalCareHistory.objects.values('attendance_sheet')
        )
    )

    class Meta:
        model = MedicalCareHistory
        fields = '__all__'
        extra_kwargs = {
            "service_date": {
                "read_only": True
            },
            "doctor_attended": {
                "read_only": True,
            }
        }


class MedicalCareHistoryDetailSerializer(serializers.ModelSerializer):
    doctor_attended = UserSerializer()
    attendance_sheet = AttendanceSheetSerializer()

    class Meta:
        model = MedicalCareHistory
        fields = [
            "attendance_sheet",
            "doctor_attended",
            "service_date"
        ]
        extra_kwargs = {
            "service_date": {
                "read_only": True
            }
        }
