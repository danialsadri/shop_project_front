from django.contrib import admin
from .models import ProductModel, ProductImageModel, ProductCategoryModel, WishlistProductModel
from jalali_date import datetime2jalali, date2jalali


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["title", "stock", "status", "price", "discount_percent", "get_created_date", "get_created_time"]
    list_filter = ["created_date"]
    raw_id_fields = ["user"]
    search_fields = ["title"]

    @admin.display(description='تاریخ ایجاد')
    def get_created_date(self, obj):
        return date2jalali(obj.created_date)

    @admin.display(description='تاریخ ایجاد')
    def get_created_time(self, obj):
        return datetime2jalali(obj.created_date).strftime('%H:%M')


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["created_date"]
    search_fields = ["title"]


@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ["product", "file"]
    list_filter = ["created_date"]
    raw_id_fields = ["product"]


@admin.register(WishlistProductModel)
class WishlistProductModelAdmin(admin.ModelAdmin):
    list_display = ["user", "product"]
    list_filter = ["created_date"]
    raw_id_fields = ["user", "product"]
