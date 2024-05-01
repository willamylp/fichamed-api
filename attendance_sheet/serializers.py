from rest_framework import serializers
from .models import AttendanceSheet


class AttendanceSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceSheet
        fields = '__all__'
