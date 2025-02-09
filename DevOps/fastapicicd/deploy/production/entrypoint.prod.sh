#!/bin/bash

echo "Applying Alembic Migrations..."
alembic upgrade head

echo "Starting Celery Worker..."
celery -A worker.celery_app worker --loglevel=info &

echo "Starting FastAPI..."
uvicorn main:app --host 0.0.0.0 --port 8000
