# Generated by Django 3.2 on 2022-12-02 07:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0007_alter_settings_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'заказ', 'verbose_name_plural': 'заказы'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='insure',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='photo',
        ),
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Количество'),
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, default=10.0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='telegram_users.telegramuser', verbose_name='Покупатель'),
        ),
    ]
