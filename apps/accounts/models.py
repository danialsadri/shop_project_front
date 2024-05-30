from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.accounts.validators import validate_iranian_cellphone_number
from django.contrib.auth.base_user import BaseUserManager
from apps.utils.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("type", UserType.superuser.value)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class UserType(models.IntegerChoices):
    customer = 1, "customer"
    admin = 2, "admin"
    superuser = 3, "superuser"


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_staff = models.BooleanField(default=False, verbose_name='ادمین')
    is_verified = models.BooleanField(default=False, verbose_name='تایید شده')
    type = models.IntegerField(choices=UserType.choices, default=UserType.customer.value, verbose_name='نوع')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email


class Profile(BaseModel):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name="user_profile", verbose_name='کاربر')
    first_name = models.CharField(max_length=255, verbose_name='نام')
    last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
    phone_number = models.CharField(max_length=12, validators=[validate_iranian_cellphone_number], verbose_name='شماره')
    image = models.ImageField(upload_to="profile/", default="profile/default.png", verbose_name='تصویر')

    def get_fullname(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        return "کاربر جدید"

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-created_date']
        indexes = [models.Index(fields=['-created_date'])]
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'
