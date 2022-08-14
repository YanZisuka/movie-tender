from datetime import datetime

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser

from django.core.cache import cache
from . import redis_key_schema


class User(AbstractUser):
    """== Schema Information
    followers :`User`
    nickname :`str`
    birth :`date`
    survey :`List[str]`
    """

    followers = models.ManyToManyField(
        "self", related_name="followings", symmetrical=False
    )

    nickname = models.CharField(max_length=20, default="")
    birth = models.DateField(default=datetime.now)
    survey = ArrayField(models.CharField(max_length=100), blank=True, default=list)

    def save(self, *args, **kwargs):
        cache.delete(redis_key_schema.user_profile(self.username))
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.delete(redis_key_schema.user_profile(self.username))
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"User {self.pk}: {self.username}"
