# app/main.py
from fastapi import FastAPI, HTTPException
from app.schemas import ItemCreate, ItemResponse
from app.crud import create_item, get_item
# Add this to app/main.py
from app.celery_worker import add
from celery.result import AsyncResult


app = FastAPI(title="My FastAPI App")

@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int):
    item = get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/", response_model=ItemResponse)
async def create_new_item(item: ItemCreate):
    return create_item(item)

@app.post("/tasks/")
async def run_task(x: int, y: int):
    task = add.delay(x, y)
    return {"task_id": task.id}

@app.get("/task/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id)
    return {"task_id": task_id, "status": task_result.status}

@app.get("/task/{task_id}/result")
async def get_task_result(task_id: str):
    task_result = AsyncResult(task_id)
    if task_result.ready():
        return {"task_id": task_id, "result": task_result.result}
    return {"task_id": task_id, "status": task_result.status, "result": None}
