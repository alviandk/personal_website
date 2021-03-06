# Generated by Django 3.0.7 on 2020-08-01 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('study', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('theme', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThesisMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentors', to='education.Thesis')),
            ],
        ),
    ]
