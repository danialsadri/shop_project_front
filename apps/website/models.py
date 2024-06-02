from django.db import models
from apps.utils.models import BaseModel


class ContactModel(BaseModel):
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    phone_number = models.CharField(max_length=200, verbose_name='شماره')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    content = models.TextField(max_length=1000, verbose_name='توضیحات')
    is_seen = models.BooleanField(default=False, verbose_name='دیده شده|نشده')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'لیست ارتباط با ما'

    def __str__(self):
        return self.full_name


class NewsLetterModel(BaseModel):
    email = models.EmailField(verbose_name='ایمیل')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'خبرنامه'
        verbose_name_plural = 'لیست خبرنامه'

    def __str__(self):
        return self.email
