# Generated by Django 5.0.7 on 2024-08-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=200, null=True)),
                ("subtitle", models.CharField(blank=True, max_length=200, null=True)),
                ("content", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
            },
        ),
    ]
