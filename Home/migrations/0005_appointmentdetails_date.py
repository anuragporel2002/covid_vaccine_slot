# Generated by Django 3.2.6 on 2023-05-10 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_appointmentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentdetails',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
