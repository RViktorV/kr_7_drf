# Generated by Django 4.2 on 2024-10-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="users",
            managers=[],
        ),
        migrations.AlterField(
            model_name="users",
            name="telegram_id",
            field=models.CharField(help_text="Введите Telegram ID", max_length=50, verbose_name="Telegram ID"),
        ),
    ]
