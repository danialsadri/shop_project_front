from django.contrib import admin
from .models import PaymentModel
from jalali_date import datetime2jalali, date2jalali


@admin.register(PaymentModel)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ["authority_id", "amount", "response_code", "status", "get_created_date", "get_created_time"]
    list_filter = ["created_date"]

    @admin.display(description='تاریخ ایجاد')
    def get_created_date(self, obj):
        return date2jalali(obj.created_date)

    @admin.display(description='تاریخ ایجاد')
    def get_created_time(self, obj):
        return datetime2jalali(obj.created_date).strftime('%H:%M')
