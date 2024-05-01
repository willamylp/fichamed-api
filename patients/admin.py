from django.contrib import admin
from django.core.paginator import Paginator
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'created_at', 'updated_at')
    list_display_links = ('id', 'patient_name')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 50
    paginator = Paginator
    search_fields = ('patient_name',)
    ordering = ('patient_name', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Informações do Paciente', {
            'fields': (
                'patient_name',
            )
        }),
    )
