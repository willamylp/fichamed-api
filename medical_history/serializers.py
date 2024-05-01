from rest_framework import serializers
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
                "read_only": True
            },
        }


class MedicalCareHistoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalCareHistory
        fields = '__all__'
