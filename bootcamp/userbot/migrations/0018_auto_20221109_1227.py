# Generated by Django 3.2 on 2022-11-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userbot', '0017_auto_20221109_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day_lesson',
            name='day',
            field=models.CharField(blank=True, choices=[('Mn', 'Понедельник'), ('Tu', 'Вторник'), ('We', 'Среда'), ('Th', 'Четверг'), ('Fr', 'Пятница')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Урок'),
        ),
    ]