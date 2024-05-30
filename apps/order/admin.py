from django.contrib import admin
from .models import OrderModel, OrderItemModel, CouponModel, UserAddressModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["user", "total_price", "coupon", "status", "created_date"]
    list_filter = ["created_date"]
    raw_id_fields = ["user"]


@admin.register(OrderItemModel)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price", "created_date"]
    list_filter = ["created_date"]
    raw_id_fields = ["order", "product"]


@admin.register(CouponModel)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ["code", "discount_percent", "max_limit_usage", "used_by_count", "expiration_date", "created_date"]
    list_filter = ["created_date"]
    search_fields = ["code"]

    def used_by_count(self, obj):
        return obj.used_by.all().count()


@admin.register(UserAddressModel)
class UserAddressModelAdmin(admin.ModelAdmin):
    list_display = ["user", "state", "city", "zip_code", "created_date"]
    list_filter = ['created_date']
    raw_id_fields = ["user"]
