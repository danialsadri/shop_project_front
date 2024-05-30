from django.contrib import admin
from .models import CartModel, CartItemModel


@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["user"]
    list_filter = ["created_date"]
    raw_id_fields = ["user"]


@admin.register(CartItemModel)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ["cart", "product", "quantity"]
    list_filter = ["created_date"]
    raw_id_fields = ["cart", "product"]
