from django.contrib import admin
from .models import PaymentModel


@admin.register(PaymentModel)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ["authority_id", "amount", "response_code", "status", "created_date"]
    list_filter = ["created_date"]
