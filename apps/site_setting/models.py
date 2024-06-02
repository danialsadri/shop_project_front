from django.db import models
from apps.utils.models import BaseModel


class FooterLinkBoxModel(BaseModel):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    active = models.BooleanField(default=False, verbose_name='فعال|غیرفعال')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLinkModel(BaseModel):
    footer_link_box = models.ForeignKey(FooterLinkBoxModel, on_delete=models.CASCADE, related_name='footer_links', verbose_name='دسته بندی')
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    url = models.URLField(max_length=1000, verbose_name='لینک')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


class SliderModel(BaseModel):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    url = models.URLField(max_length=1000, verbose_name='لینک')
    image = models.ImageField(upload_to='slider/', verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال|غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title
