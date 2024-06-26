# Generated by Django 5.0.6 on 2024-05-30 01:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='آیدی')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبد خرید ها',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='CartItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='آیدی')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='تعداد')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.productmodel', verbose_name='محصول')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='cart.cartmodel', verbose_name='سبد خرید')),
            ],
            options={
                'verbose_name': 'آیتم سبد خرید',
                'verbose_name_plural': 'آیتم سبد خرید ها',
                'ordering': ['-created_date'],
            },
        ),
        migrations.AddIndex(
            model_name='cartmodel',
            index=models.Index(fields=['-created_date'], name='cart_cartmo_created_3afda1_idx'),
        ),
        migrations.AddIndex(
            model_name='cartitemmodel',
            index=models.Index(fields=['-created_date'], name='cart_cartit_created_8f6f3e_idx'),
        ),
    ]
