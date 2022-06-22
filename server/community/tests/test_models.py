from django.test import TestCase

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
            cls.reviews.append(ReviewFactory.build(movie=cls.movie, user=cls.user))
        Review.objects.bulk_create(cls.reviews)

    def test_오프셋_페이징을_할수있다(self):
        self.assertEqual(list(Review.objects.paginated_v2(1)), list(Review.objects.raw("""SELECT "community_review"."id",
       "community_review"."user_id",
       "community_review"."movie_id",
       "community_review"."content",
       "community_review"."created_at",
       "community_review"."updated_at"
  FROM "community_review"
 ORDER BY "community_review"."id" DESC
 LIMIT 5""")))

    def test_개선된_오프셋_페이징을_할수있다(self):
        self.assertEqual(list(Review.objects.paginated_v2(1)), list(Review.objects.raw("""SELECT "community_review"."id",
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
 ORDER BY "community_review"."id" DESC""")))

    def test_커서_페이징을_할수있다(self):
        self.assertEqual(list(Review.objects.cursor_paginated(100)), list(Review.objects.raw("""SELECT "community_review"."id",
       "community_review"."user_id",
       "community_review"."movie_id",
       "community_review"."content",
       "community_review"."created_at",
       "community_review"."updated_at"
  FROM "community_review"
 WHERE "community_review"."id" <= 100
 ORDER BY "community_review"."id" DESC
 LIMIT 5""")))


class CommentTest(TestCase):
    pass