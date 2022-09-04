from celery import shared_task
from .factories import MovieFactory


@shared_task
def seed_movies(page_num: int = 100):
    MovieFactory().api.seed(page_num)
