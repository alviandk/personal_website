# Generated by Django 3.1 on 2020-08-21 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_project', '0003_aplication_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aplication',
            new_name='Project',
        ),
    ]