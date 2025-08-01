# Generated by Django 5.2.4 on 2025-07-16 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('age_group', models.CharField(choices=[('U1', 'Under 1 Year'), ('U5', 'Under 5 Years'), ('A5', 'Above 5 Years')], max_length=2)),
                ('male', models.PositiveIntegerField(default=0)),
                ('female', models.PositiveIntegerField(default=0)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.disease')),
            ],
            options={
                'unique_together': {('disease', 'date', 'age_group')},
            },
        ),
    ]
