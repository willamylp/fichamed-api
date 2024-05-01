from rest_framework import serializers
from .models import AttendanceSheet


class AttendanceSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceSheet
        fields = [
            "card_number",
            "patient_name",
            "filled_by",
            "classification",
            "clinical_history"
        ]
