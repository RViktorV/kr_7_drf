# Generated by Django 4.2 on 2024-10-07 06:11

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_users_managers_alter_users_telegram_id"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="users",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]