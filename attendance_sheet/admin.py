from django.contrib import admin
from django.core.paginator import Paginator
from .models import AttendanceSheet


@admin.register(AttendanceSheet)
class AttendanceSheetAdmin(admin.ModelAdmin):
    list_display = ["id", "card_number", "patient_name", "filled_by", "classification", "created_at", "updated_at"]
    list_display_links = ["id", "card_number", "patient_name"]
    list_filter = ["id", "filled_by", "patient_name", "classification", "created_at", "updated_at"]
    list_per_page = 50
    paginator = Paginator
    search_fields = ["card_number", "patient", "filled_by", "doctor_attended", "classification", "created_at", "updated_at"]
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
    fieldsets = [
        ("Ficha de Atendimento", {
            "fields": (
                "card_number",
                "patient_name",
                "filled_by",
                "classification",
                "clinical_history"
            )
        }),
    ]

    readonly_fields = ["created_at", "updated_at"]
