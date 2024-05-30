from django.contrib import admin
from .models import ProductModel, ProductImageModel, ProductCategoryModel, WishlistProductModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["title", "stock", "status", "price", "discount_percent", "created_date"]
    list_filter = ["created_date"]
    raw_id_fields = ["user"]
    search_fields = ["title"]


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
