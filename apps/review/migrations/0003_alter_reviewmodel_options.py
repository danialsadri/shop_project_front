# Generated by Django 5.0.6 on 2024-07-29 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_reviewmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewmodel',
            options={'ordering': ['-created_date'], 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
    ]
