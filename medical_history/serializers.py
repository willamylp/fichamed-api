from rest_framework import serializers
from .models import MedicalCareHistory


class MedicalCareHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalCareHistory
        fields = ["attendance_sheet", "doctor_attended",]
