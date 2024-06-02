from django.contrib import admin
from .models import *


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["email", "phone_number", "subject", "is_seen"]
    list_filter = ["created_date"]
    search_fields = ["email"]


@admin.register(NewsLetterModel)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ["email"]
    list_filter = ["created_date"]
    search_fields = ["email"]
