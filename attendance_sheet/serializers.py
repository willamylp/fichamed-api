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
            "clinical_history",
            "created_at",
            "updated_at"
        ]
        extra_kwargs = {
            "filled_by": {
                "read_only": True
            },
            "created_at": {
                "read_only": True
            },
            "updated_at": {
                "read_only": True
            },
        }
