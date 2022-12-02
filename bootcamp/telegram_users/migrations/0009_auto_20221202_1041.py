# Generated by Django 3.2 on 2022-12-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0008_auto_20221202_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Итоговая стоимость в руб.'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Стоимость за единицу в валюте'),
        ),
    ]
