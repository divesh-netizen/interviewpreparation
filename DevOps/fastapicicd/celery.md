# Celery: A Powerful Distributed Task Queue

## Introduction
Celery is an asynchronous task queue based on distributed message passing. It is primarily used for executing background tasks, scheduling jobs, and handling task distribution across multiple workers.

---

## 1. Background Task Processing (Async Jobs)
Celery allows you to offload time-consuming operations to the background, preventing blocking of API requests.

### Example: Sending Emails Asynchronously
```python
from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def send_email(to_email: str, subject: str, body: str):
    import time
    time.sleep(5)
    return f"Email sent to {to_email} with subject {subject}"
```

✅ The API sends an email without blocking the request.

---

## 2. Task Scheduling (Periodic Tasks)
Celery allows you to execute tasks at specified intervals using Celery Beat.

### Example: Running a Daily Database Cleanup
```python
from celery import Celery
from celery.schedules import crontab

celery_app = Celery("tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

@celery_app.task
def cleanup_db():
    return "Database Cleanup Done!"

# Schedule the task to run daily at midnight
celery_app.conf.beat_schedule = {
    "cleanup-every-midnight": {
        "task": "tasks.cleanup_db",
        "schedule": crontab(hour=0, minute=0),
    },
}
```

✅ The task will automatically run every midnight.

---

## 3. Task Chaining & Workflows
Celery supports sequential execution of multiple tasks.

### Example: Image Processing Pipeline
```python
from celery import Celery, chain

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def download_image(image_url):
    return f"Downloaded {image_url}"

@celery_app.task
def resize_image(image_path):
    return f"Resized {image_path}"

@celery_app.task
def upload_image(image_path):
    return f"Uploaded {image_path}"

# Chaining tasks together
task_chain = chain(download_image.s("http://image.com/photo.jpg") | resize_image.s() | upload_image.s())
task_chain.apply_async()
```

✅ The image will be downloaded → resized → uploaded automatically.

---

## 4. Task Prioritization & Rate Limiting
Celery allows assigning priorities to tasks and limiting their execution rate.

### Example: Assigning High & Low Priority Queues
```python
@celery_app.task(queue="high_priority")
def critical_task():
    return "High priority task completed"

@celery_app.task(queue="low_priority")
def slow_task():
    return "Low priority task completed"
```

✅ You can start different workers for different queues.

```sh
celery -A tasks worker --queues=high_priority --loglevel=info
celery -A tasks worker --queues=low_priority --loglevel=info
```

---

## 5. Distributed Task Execution (Scaling Workers)
Celery supports running workers across multiple servers.

### Example: Running Celery Workers on Different Servers
```sh
# Start worker on Server 1
celery -A tasks worker --loglevel=info --hostname=worker1@%h

# Start worker on Server 2
celery -A tasks worker --loglevel=info --hostname=worker2@%h
```

✅ The workload will be distributed across multiple machines.

---

## 6. Error Handling & Retries
Celery can automatically retry failed tasks.

### Example: Retrying Failed API Requests
```python
from celery import Celery
from celery.exceptions import MaxRetriesExceededError

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task(bind=True, max_retries=3)
def fetch_data(self, url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as exc:
        raise self.retry(exc=exc, countdown=5)  # Retry in 5 seconds
```

✅ If the API fails, Celery will automatically retry the request.

---

## 7. Task Expiration & Time Limits
Celery allows setting time limits and expiring old tasks.

### Example: Auto-Failing a Task if it Takes Too Long
```python
@celery_app.task(time_limit=10)
def slow_function():
    import time
    time.sleep(20)  # Task will be killed after 10 seconds
```

✅ If the task takes more than 10 seconds, Celery automatically kills it.

---

## Summary: What Can Celery Do?

| Feature                 | Use Case                                   |
|------------------------|------------------------------------------|
| **Background Tasks**   | Offload heavy computations & async tasks |
| **Task Scheduling**    | Run periodic jobs (e.g., database cleanup) |
| **Task Chaining**      | Create workflows (e.g., image processing) |
| **Prioritization**     | Assign high & low priority queues |
| **Distributed Execution** | Run Celery on multiple servers |
| **Auto-Retries**       | Retry failed tasks (e.g., failed API requests) |
| **Time Limits**        | Kill tasks if they run too long |
| **Task Expiration**    | Auto-remove old tasks |

Celery is a powerful tool for task management, scaling, and automation. 🚀

