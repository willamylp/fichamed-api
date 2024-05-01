from rest_framework import serializers
from .models import AttendanceSheet


class AttendanceSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceSheet
        fields = "__all__"
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


class AttendanceSheetDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceSheet
        fields = "__all__"
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


class AttendanceSheetPanelSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceSheet
        fields = [
            "id",
            "card_number",
            "patient_name",
            "classification",
            "created_at"
        ]
