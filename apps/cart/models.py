from django.db import models
from apps.utils.models import BaseModel


class CartModel(BaseModel):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, verbose_name='کاربر')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید ها'

    def __str__(self):
        return self.user.email

    def calculate_total_price(self):
        return sum(item.product.get_price() * item.quantity for item in self.cart_items.all())


class CartItemModel(BaseModel):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, related_name="cart_items", verbose_name='سبد خرید')
    product = models.ForeignKey('shop.ProductModel', on_delete=models.PROTECT, verbose_name='محصول')
    quantity = models.PositiveIntegerField(default=0, verbose_name='تعداد')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'آیتم سبد خرید'
        verbose_name_plural = 'آیتم سبد خرید ها'

    def __str__(self):
        return f"{self.product.title} - {self.cart.id}"
