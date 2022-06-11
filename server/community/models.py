from datetime import timedelta

from django.db import models
from django.conf import settings
from movies.models import Movie


class Review(models.Model):
    """ == Schema Information
    user :`User`
    movie :`Movie`
    like_users :`User`
    content :`str`
    created_at :`datetime`
    updated_at :`datetime`
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_modified(self):
        return abs(self.created_at - self.updated_at) > timedelta(seconds=1)

    def __str__(self):
        return f"Review {self.pk}: {self.user}'s review for {self.movie}"


class Comment(models.Model):
    """ == Schema Information
    user :`User`
    review :`Review`
    content :`str`
    created_at :`datetime`
    updated_at :`datetime`
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_modified(self):
        return abs(self.created_at - self.updated_at) > timedelta(seconds=1)

    def __str__(self):
        return f"Comment {self.pk}: {self.user}'s comment for {self.review}"
