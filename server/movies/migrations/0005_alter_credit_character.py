# Generated by Django 4.0.6 on 2022-08-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_movies_movi_keyword_afd773_gin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='character',
            field=models.CharField(max_length=300),
        ),
    ]
