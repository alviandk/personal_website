# Generated by Django 3.0.7 on 2020-08-01 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_journey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='accomplishment',
            field=models.ManyToManyField(blank=True, related_name='experiences', to='my_journey.Accomplishment'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
