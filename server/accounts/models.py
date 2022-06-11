from datetime import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ == Schema Information
    followers :`User`
    nickname :`str`
    birth :`date`
    survey :`List[str]`
    """
    
    followers = models.ManyToManyField('self', related_name='followings', symmetrical=False)

    nickname = models.CharField(max_length=20, default='')
    birth = models.DateField(default=datetime.now)
    survey = ArrayField(models.CharField(max_length=100), blank=True, default=list)

    def __str__(self):
        return f'User {self.pk}: {self.username}'
