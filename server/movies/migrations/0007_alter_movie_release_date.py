# Generated by Django 4.0.6 on 2022-08-30 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_remove_movie_movies_movi_keyword_afd773_gin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(),
        ),
    ]
