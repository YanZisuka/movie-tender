from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    follows = models.ManyToManyField('self', related_name='followings', symmetrical=False)
    survey = ArrayField(models.CharField(max_length=100), blank=True)

    def __str__(self):
        return f'User {self.pk}: {self.username}'
