import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

app = Celery(
    "tasks", broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND
)

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "seed_movies_every_day": {
        "task": "movies.tasks.seed_movies",
        "schedule": crontab(hour="6", minute="0"),
        "args": (100,),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
