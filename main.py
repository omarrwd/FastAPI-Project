from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# MongoDB connection
client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/<database>?retryWrites=true&w=majority")
db = client["task_db"]
collection = db["tasks"]

class Task(BaseModel):
    title: str
    description: str
    file_name: str
    completed: bool = False

def get_db():
    yield db

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tasks")
def get_tasks(db = Depends(get_db)):
    tasks = []
    for task in db.tasks.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    return tasks

@app.post("/tasks")
def create_task(task: Task, db = Depends(get_db)):
    result = db.tasks.insert_one(task.dict())
    return {"id": str(result.inserted_id)}

@app.get("/tasks/{task_id}")
def get_task(task_id: str, db = Depends(get_db)):
    task = db.tasks.find_one({"_id": ObjectId(task_id)})
    if task:
        task["_id"] = str(task["_id"])
        return task
    return {"error": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: str, updated_task: Task, db = Depends(get_db)):
    result = db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": updated_task.dict()})
    if result.modified_count:
        return {"message": "Task updated"}
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, db = Depends(get_db)):
    result = db.tasks.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count:
        return {"message": "Task deleted"}
    return {"error": "Task not found"}
