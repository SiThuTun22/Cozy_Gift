# Generated by Django 5.1 on 2025-01-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="plaintext_password",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]