# Generated by Django 3.2.6 on 2023-05-10 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.TextField(max_length=25, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='StateName',
            fields=[
                ('name', models.TextField(max_length=25, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineCentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=75)),
                ('working_hour', models.TimeField()),
                ('address', models.TextField(max_length=250)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.city')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.statename'),
        ),
    ]
