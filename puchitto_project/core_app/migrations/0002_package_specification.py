# Generated by Django 5.0.1 on 2024-01-12 01:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='specification',
            field=ckeditor.fields.RichTextField(default='詳細'),
        ),
    ]