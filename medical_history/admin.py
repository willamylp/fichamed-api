from django.contrib import admin
from django.core.paginator import Paginator
from .models import MedicalCareHistory


@admin.register(MedicalCareHistory)
class MedicalCareHistoryAdmin(admin.ModelAdmin):
    list_display = ["id", "attendance_sheet", "doctor_attended", "service_date"]
    list_display_links = ["id", "attendance_sheet", "doctor_attended"]
    list_filter = ["id", "attendance_sheet", "doctor_attended", "service_date"]
    list_per_page = 50
    paginator = Paginator
    search_fields = ["attendance_sheet", "doctor_attended", "service_date"]
    date_hierarchy = "service_date"
    ordering = ["service_date"]
    readonly_fields = ["service_date"]
    fieldsets = (
        ('Informações do Atendimento', {
            "fields": (
                "attendance_sheet",
                "doctor_attended",
            ),
        }),
    )
    
