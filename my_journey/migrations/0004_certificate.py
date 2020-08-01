# Generated by Django 3.0.7 on 2020-08-01 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_journey', '0003_competition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='my_journey.Competition')),
            ],
        ),
    ]
