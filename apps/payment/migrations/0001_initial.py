# Generated by Django 5.0.6 on 2024-05-30 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='آیدی')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('authority_id', models.CharField(max_length=255, verbose_name='شناسه مرجع')),
                ('ref_id', models.BigIntegerField(blank=True, null=True, verbose_name='آیدی مرجع')),
                ('amount', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='میزان')),
                ('response_json', models.JSONField(default=dict, verbose_name='پاسخ json')),
                ('response_code', models.IntegerField(blank=True, null=True, verbose_name='کد پاسخ')),
                ('status', models.IntegerField(choices=[(1, 'در انتظار'), (2, 'پرداخت موفق'), (3, 'پرداخت ناموفق')], default=1, verbose_name='وضعیت')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
