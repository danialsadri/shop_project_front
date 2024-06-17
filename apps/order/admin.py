from django.contrib import admin
from .models import OrderModel, OrderItemModel, CouponModel, UserAddressModel
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemModelInline(admin.StackedInline):
    model = OrderItemModel
    extra = 0
    show_change_link = True
    classes = ['collapse']
    autocomplete_fields = ["order", "product"]


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["user", "total_price", "coupon", "status"]
    list_filter = ["created_date"]
    search_fields = ["user__email"]
    autocomplete_fields = ["user", "payment", "coupon"]
    inlines = [OrderItemModelInline]


@admin.register(OrderItemModel)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price"]
    list_filter = ["created_date"]
    autocomplete_fields = ["order", "product"]


@admin.register(UserAddressModel)
class UserAddressModelAdmin(admin.ModelAdmin):
    list_display = ["user", "state", "city", "zip_code"]
    list_filter = ['created_date']
    search_fields = ["user__email"]
    autocomplete_fields = ["user"]


@admin.register(CouponModel)
class CouponModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ["code", "discount_percent", "max_limit_usage", "used_by_count", "get_expiration_date", "get_expiration_time"]
    list_filter = ["created_date"]
    search_fields = ["code"]
    autocomplete_fields = ["used_by"]

    def used_by_count(self, obj):
        return obj.used_by.all().count()

    @admin.display(description='تاریخ انقضا')
    def get_expiration_date(self, obj):
        return date2jalali(obj.expiration_date)

    @admin.display(description='تاریخ انقضا')
    def get_expiration_time(self, obj):
        return datetime2jalali(obj.expiration_date).strftime('%H:%M')
