from django.test import TestCase
from django.db import connection

from .factories import ReviewFactory
from accounts.tests.factories import UserFactory
from movies.tests.factories import MovieFactory

from ..models import Review, Comment


class ReviewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory.create(password='qwer`123')
        cls.movie = MovieFactory.create()
        cls.reviews = []
        for _ in range(100):
            cls.reviews.append(ReviewFactory.create(movie=cls.movie, user=cls.user))

    def test_오프셋_페이징을_할수있다(self):
        self.assertEqual(Review.objects.paginated_v2(1), Review.objects.raw("""SELECT "community_review"."id",
       "community_review"."user_id",
       "community_review"."movie_id",
       "community_review"."content",
       "community_review"."created_at",
       "community_review"."updated_at"
  FROM "community_review"
 ORDER BY "community_review"."id" DESC
 LIMIT 5"""))

    def test_개선된_오프셋_페이징을_할수있다(self):
        def queryset():
            with connection.cursor() as cursor:
                cursor.execute("""SELECT "community_review"."id",
       "community_review"."user_id",
       "community_review"."movie_id",
       "community_review"."content",
       "community_review"."created_at",
       "community_review"."updated_at"
  FROM "community_review"
 WHERE "community_review"."id" IN (
        SELECT "community_review"."id"
          FROM "community_review"
         ORDER BY "community_review"."id" DESC
         LIMIT 5
       )
 ORDER BY "community_review"."id" DESC""")
            return cursor.fetchone()
        self.assertEqual(Review.objects.paginated_v2(1), queryset())

    def test_커서_페이징을_할수있다(self):
        self.assertEqual(Review.objects.cursor_paginated(35), Review.objects.raw("""SELECT "community_review"."id",
       "community_review"."user_id",
       "community_review"."movie_id",
       "community_review"."content",
       "community_review"."created_at",
       "community_review"."updated_at"
  FROM "community_review"
 WHERE "community_review"."id" < 35
 ORDER BY "community_review"."id" DESC
 LIMIT 5"""))


class CommentTest(TestCase):
    pass