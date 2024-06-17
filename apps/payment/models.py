from django.db import models
from apps.utils.models import BaseModel


class PaymentStatusType(models.IntegerChoices):
    pending = 1, "در انتظار"
    success = 2, "پرداخت موفق"
    failed = 3, "پرداخت ناموفق"


class PaymentModel(BaseModel):
    authority_id = models.CharField(max_length=255, verbose_name='شناسه مرجع')
    ref_id = models.BigIntegerField(null=True, blank=True, verbose_name='آیدی مرجع')
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name='قیمت')
    response_json = models.JSONField(default=dict, verbose_name='پاسخ json')
    response_code = models.IntegerField(null=True, blank=True, verbose_name='کد پاسخ')
    status = models.IntegerField(choices=PaymentStatusType.choices, default=PaymentStatusType.pending.value, verbose_name='وضعیت')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت ها'

    def __str__(self):
        return self.authority_id
