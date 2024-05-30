from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from apps.utils.models import BaseModel


class ReviewStatusType(models.IntegerChoices):
    pending = 1, "در انتظار تایید"
    accepted = 2, "تایید شده"
    rejected = 3, "رد شده"


class ReviewModel(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='کاربر')
    product = models.ForeignKey('shop.ProductModel', on_delete=models.CASCADE, verbose_name='محصول')
    description = models.TextField(verbose_name='توضیحات')
    rate = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='امتیاز')
    status = models.IntegerField(choices=ReviewStatusType.choices, default=ReviewStatusType.pending.value, verbose_name='وضعیت')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'بازدید'
        verbose_name_plural = 'بازدید ها'

    def __str__(self):
        return f"{self.user} - {self.product.id}"

    def get_status(self):
        return {
            "id": self.status,
            "title": ReviewStatusType(self.status).name,
            "label": ReviewStatusType(self.status).label,
        }
