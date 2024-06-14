from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin
from django.contrib.sessions.models import Session
from .models import Profile, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "is_superuser", "is_active", "is_verified"]
    list_filter = ["email", "is_superuser", "is_active", "is_verified"]
    searching_fields = ["email"]
    ordering = ["email"]
    fieldsets = (
        (
            "Authentication",
            {"fields": ["email", "password"]},
        ),
        (
            "permissions",
            {"fields": ["is_staff", "is_active", "is_superuser", "is_verified"]},
        ),
        (
            "group permissions",
            {"fields": ["groups", "user_permissions", "type"]},
        ),
        (
            "important date",
            {"fields": ["last_login"]},
        ),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ["email", "password1", "password2", "is_staff", "is_active", "is_superuser", "is_verified", "type"]},
        ),
    )


@admin.register(Profile)
class CustomProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name", "last_name", "phone_number"]
    list_filter = ['created_date']
    search_fields = ["first_name", "last_name", "phone_number"]
    raw_id_fields = ["user"]


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'action_time', 'action_flag']
    list_filter = ['action_time']
    search_fields = ['user__email']
