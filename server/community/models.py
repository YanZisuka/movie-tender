from django.db import models
from django.conf import settings
from movies.models import Movie


class Review(models.Model):
    """content (`str`), created_at (`date`), updated_at(`date`), user (class `User`), movie (class `Movie`)
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review {self.pk}: {self.user}'s review for {self.movie}"


class Comment(models.Model):
    """content (`str`), created_at (`date`), updated_at(`date`), user (class `User`), review (class `Review`)
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment {self.pk}: {self.user}'s comment for {self.review}"
