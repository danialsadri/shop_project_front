# Generated by Django 5.0.6 on 2024-05-30 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='آیدی')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام')),
                ('email', models.EmailField(default=None, max_length=254, null=True, verbose_name='ایمیل')),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='شماره')),
                ('subject', models.CharField(blank=True, max_length=200, null=True, verbose_name='موضوع')),
                ('content', models.TextField(max_length=700, verbose_name='توضیحات')),
                ('is_seen', models.BooleanField(default=False, verbose_name='دیده شده|نشده')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='آیدی')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
