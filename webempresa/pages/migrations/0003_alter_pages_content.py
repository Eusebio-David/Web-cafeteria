# Generated by Django 5.0.7 on 2024-08-12 22:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0002_alter_pages_options_pages_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pages",
            name="content",
            field=ckeditor.fields.RichTextField(verbose_name="Contendio"),
        ),
    ]