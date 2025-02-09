# celery_worker.py
from celery import Celery
import os
import time

broker_url = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",  # Message Queue
    backend="redis://localhost:6379/0"  # Result Storage
)

@celery_app.task
def add(x, y):
    time.sleep(120)  # Delay execution for 2 minutes
    return x + y
