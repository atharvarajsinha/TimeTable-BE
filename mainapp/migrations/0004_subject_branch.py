# Generated by Django 5.1.3 on 2024-11-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_alter_room_room_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="branch",
            field=models.CharField(default="", max_length=100),
        ),
    ]
