from datetime import timedelta

from django.db import models
from django.conf import settings

from django.core.cache import cache
from . import redis_key_schema

from movies.models import Movie


class ReviewQuerySet(models.QuerySet):
    def paginated(self, page: int, page_size: int = 5):
        limit = (page - 1) * page_size
        return self[limit : limit + page_size]

    def paginated_v2(self, page: int, page_size: int = 5):
        index_only_scan = self.paginated(page, page_size)
        return self.filter(id__in=index_only_scan)

    def cursor_paginated(self, cursor: int, page_size: int = 5):
        return self.filter(id__lt=cursor)[ : page_size]


class Review(models.Model):
    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'], include=[], name='idx_review_iddesc')
        ]
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

    objects = ReviewQuerySet.as_manager()

    def flush_cache(self, prefix: str):
        for key in cache.iter_keys(prefix):
            cache.delete(key)

    def save(self, *args, **kwargs):
        self.flush_cache('reviews:*')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.flush_cache('reviews:*')
        super().delete(*args, **kwargs)

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

    def flush_cache(self, prefix: str):
        for key in cache.iter_keys(prefix):
            cache.delete(key)

    def save(self, *args, **kwargs):
        self.flush_cache('reviews:*')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.flush_cache('reviews:*')
        super().delete(*args, **kwargs)

    @property
    def is_modified(self):
        return abs(self.created_at - self.updated_at) > timedelta(seconds=1)

    def __str__(self):
        return f"Comment {self.pk}: {self.user}'s comment for {self.review}"
