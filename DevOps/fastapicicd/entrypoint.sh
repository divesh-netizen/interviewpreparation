#!/bin/bash

echo "Running Database Migrations..."
alembic revision --autogenerate -m "Auto Migration"

if alembic upgrade head; then
    echo "Migrations applied successfully!"
else
    echo "Migration failed! Rolling back..."
    alembic downgrade -1
    exit 1
fi

# Start Celery worker in background
echo "Starting Celery Worker..."
celery -A worker.celery_app worker --loglevel=info &

# Start FastAPI server
echo "Starting FastAPI..."
uvicorn main:app --host 0.0.0.0 --port 8000
