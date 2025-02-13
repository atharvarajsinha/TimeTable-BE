# Generated by Django 5.1.3 on 2025-02-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0011_alter_teacher_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="is_special_subject",
            field=models.CharField(default="No", max_length=10),
        ),
        migrations.AddField(
            model_name="subject",
            name="weekly_quota_limit",
            field=models.IntegerField(default=1),
        ),
    ]
