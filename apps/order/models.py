from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from apps.utils.models import BaseModel


class OrderStatusType(models.IntegerChoices):
    pending = 1, "در انتظار پرداخت"
    success = 2, "موفقیت آمیز"
    failed = 3, "لغو شده"


class UserAddressModel(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='کاربر')
    address = models.CharField(max_length=250, verbose_name='آدرس')
    state = models.CharField(max_length=50, verbose_name='استان')
    city = models.CharField(max_length=50, verbose_name='شهر')
    zip_code = models.CharField(max_length=50, verbose_name='کد پستی')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    def __str__(self):
        return self.user.email


class CouponModel(BaseModel):
    used_by = models.ManyToManyField('accounts.User', related_name="coupon_users", blank=True, verbose_name='استفاده شده توسط')
    code = models.CharField(max_length=100, verbose_name='کد')
    discount_percent = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='درصد تخفیف')
    max_limit_usage = models.PositiveIntegerField(default=10, verbose_name='حداکثر میزان استفاده')
    expiration_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ انقضا')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'کوپن'
        verbose_name_plural = 'کوپن ها'

    def __str__(self):
        return self.code


class OrderModel(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, verbose_name='کاربر')
    payment = models.ForeignKey('payment.PaymentModel', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='پرداخت')
    coupon = models.ForeignKey(CouponModel, on_delete=models.PROTECT, null=True, blank=True, verbose_name='کوپن')
    address = models.CharField(max_length=250, verbose_name='آدرس')
    state = models.CharField(max_length=50, verbose_name='استان')
    city = models.CharField(max_length=50, verbose_name='شهر')
    zip_code = models.CharField(max_length=50, verbose_name='کد پستی')
    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name='قیمت کل')
    status = models.IntegerField(choices=OrderStatusType.choices, default=OrderStatusType.pending.value, verbose_name='وضعیت')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'

    def __str__(self):
        return f"{self.user.email} - {self.id}"

    def calculate_total_price(self):
        return sum(item.price * item.quantity for item in self.order_items.all())

    def get_status(self):
        return {
            "id": self.status,
            "title": OrderStatusType(self.status).name,
            "label": OrderStatusType(self.status).label,
        }

    def get_full_address(self):
        return f"{self.state},{self.city},{self.address}"

    @property
    def is_successful(self):
        return self.status == OrderStatusType.success.value

    def get_price(self):
        if self.coupon:
            return round(self.total_price - (self.total_price * Decimal(self.coupon.discount_percent / 100)))
        else:
            return self.total_price


class OrderItemModel(BaseModel):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="order_items", verbose_name='سفارش')
    product = models.ForeignKey('shop.ProductModel', on_delete=models.PROTECT, verbose_name='محصول')
    quantity = models.PositiveIntegerField(default=0, verbose_name='تعداد')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name='قیمت')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'آیتم سفارش'
        verbose_name_plural = 'آیتم سفارش ها'

    def __str__(self):
        return f"{self.product.title} - {self.order.id}"
