from django.contrib import admin
from .models import OrderModel, OrderItemModel, CouponModel, UserAddressModel


class OrderItemModelInline(admin.StackedInline):
    model = OrderItemModel
    extra = 0
    show_change_link = True
    classes = ['collapse']
    raw_id_fields = ["order", "product"]


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["user", "total_price", "coupon", "status"]
    list_filter = ["created_date"]
    search_fields = ["user__email"]
    raw_id_fields = ["user", "payment", "coupon"]
    inlines = [OrderItemModelInline]


@admin.register(OrderItemModel)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price"]
    list_filter = ["created_date"]
    search_fields = ["order__user__email"]
    raw_id_fields = ["order", "product"]


@admin.register(UserAddressModel)
class UserAddressModelAdmin(admin.ModelAdmin):
    list_display = ["user", "state", "city", "zip_code"]
    list_filter = ['created_date']
    search_fields = ["user__email"]
    raw_id_fields = ["user"]


@admin.register(CouponModel)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ["code", "discount_percent", "max_limit_usage", "used_by_count", "expiration_date"]
    list_filter = ["created_date"]
    search_fields = ["code"]

    def used_by_count(self, obj):
        return obj.used_by.all().count()
