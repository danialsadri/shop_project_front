from django.contrib import admin
from .models import ReviewModel
from jalali_date import datetime2jalali, date2jalali


@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "rate", "status", "get_created_date", "get_created_time"]
    list_filter = ["created_date"]
    raw_id_fields = ["user", "product"]

    @admin.display(description='تاریخ ایجاد')
    def get_created_date(self, obj):
        return date2jalali(obj.created_date)

    @admin.display(description='تاریخ ایجاد')
    def get_created_time(self, obj):
        return datetime2jalali(obj.created_date).strftime('%H:%M')
