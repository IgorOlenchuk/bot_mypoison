# Generated by Django 3.2 on 2022-11-25 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userbot', '0023_auto_20221111_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day_lesson',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userbot.lesson'),
        ),
    ]