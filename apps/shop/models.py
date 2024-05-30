from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from apps.utils.models import BaseModel


class ProductStatusType(models.IntegerChoices):
    publish = 1, "نمایش"
    draft = 2, "عدم نمایش"


class ProductCategoryModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(allow_unicode=True, unique=True, verbose_name='اسلاگ')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصول ها'

    def __str__(self):
        return self.title


class ProductModel(BaseModel):
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT, verbose_name='کاربر')
    category = models.ManyToManyField(ProductCategoryModel, verbose_name='دسته بندی')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(allow_unicode=True, unique=True, verbose_name='اسلاگ')
    image = models.ImageField(default="/default/product-image.png", upload_to="product/img/", verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    brief_description = models.TextField(null=True, blank=True, verbose_name='توضیح مختصر')
    stock = models.PositiveBigIntegerField(default=0, verbose_name='موجودی')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name='قیمت')
    discount_percent = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='درصد تخفیف')
    avg_rate = models.FloatField(default=0.0, verbose_name='میانگین نرخ')
    status = models.IntegerField(choices=ProductStatusType.choices, default=ProductStatusType.draft.value, verbose_name='وضعیت')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصول ها'

    def __str__(self):
        return self.title

    def get_price(self):
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)

    def is_discounted(self):
        return self.discount_percent != 0

    def is_published(self):
        return self.status == ProductStatusType.publish.value


class ProductImageModel(BaseModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_images", verbose_name='محصول')
    file = models.ImageField(upload_to="product/extra-img/", verbose_name='فایل')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصویر محصول ها'

    def __str__(self):
        return self.product.title


class WishlistProductModel(BaseModel):
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT, verbose_name='کاربر')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'لیست علاقه مندی محصول'
        verbose_name_plural = 'لیست علاقه مندی ها'

    def __str__(self):
        return self.product.title
