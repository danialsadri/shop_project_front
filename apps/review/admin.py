from django.contrib import admin
from .models import ReviewModel


@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "rate", "status", "created_date"]
    list_filter = ["created_date"]
    raw_id_fields = ["user", "product"]
