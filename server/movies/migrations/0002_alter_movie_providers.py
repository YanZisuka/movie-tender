# Generated by Django 3.2.12 on 2022-05-23 00:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='providers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), blank=True, default=list, size=None),
        ),
    ]
