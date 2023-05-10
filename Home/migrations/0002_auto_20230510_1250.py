# Generated by Django 3.2.6 on 2023-05-10 07:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinecentre',
            name='working_hour',
        ),
        migrations.AddField(
            model_name='vaccinecentre',
            name='working_hour_end',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vaccinecentre',
            name='working_hour_start',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]