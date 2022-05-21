from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    followers = models.ManyToManyField('self', related_name='followings', symmetrical=False)

    survey = ArrayField(models.CharField(max_length=100), blank=True, default=list)

    def add_survey(self, kwrd: str):
        self.survey.append(kwrd)
        self.save(update_fields=['survey'])
        return self.survey

    def clear_survey(self):
        self.survey = []
        self.save(update_fields=['survey'])
        return self.survey

    def __str__(self):
        return f'User {self.pk}: {self.username}'
