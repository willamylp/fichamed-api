from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at']
    list_display_links = ['id', 'full_name', 'username', 'email']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at']
    search_fields = ['full_name', 'username', 'email']
    ordering = ['full_name', 'username', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at']
    actions = ['activate_users', 'deactivate_users']

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    activate_users.short_description = "Ativar Usuários"

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_users.short_description = "Desativar Usuários"
