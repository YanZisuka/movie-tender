# Generated by Django 4.0.6 on 2022-07-08 03:11

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20220611_1902'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='movie',
            index=django.contrib.postgres.indexes.GinIndex(fields=['_keywords'], name='movies_movi_keyword_afd773_gin'),
        ),
    ]
