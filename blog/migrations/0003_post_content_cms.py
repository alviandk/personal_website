# Generated by Django 3.1 on 2021-01-30 16:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_cms',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
