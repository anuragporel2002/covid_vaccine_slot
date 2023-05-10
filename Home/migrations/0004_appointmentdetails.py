# Generated by Django 3.2.6 on 2023-05-10 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_vaccinecentre_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('centre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.vaccinecentre')),
            ],
        ),
    ]