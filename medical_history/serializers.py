from rest_framework import serializers
from .models import MedicalCareHistory


class MedicalCareHistorySerializer(serializers.ModelSerializer):

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
            },
            "doctor_attended": {
                "read_only": True
            }
        }
