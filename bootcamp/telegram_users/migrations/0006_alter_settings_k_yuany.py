# Generated by Django 3.2 on 2022-12-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0005_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='k_yuany',
            field=models.FloatField(blank=True, null=True, verbose_name='Коэф-т к курсы'),
        ),
    ]
