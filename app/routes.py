from flask import (Flask,request)
from app,database import task
app = Flask(__name__) 

@app.get("/")
def home():
    me = {
        "first_name":"Mauricio",
        "last_name":"Navarro",
        "hobbies": "Watch TV",
        "is_inline": True
    }
    return me

@app.get("/task")
def scan():
    out={
        "task":task.scan(),
        "ok":True
    }
    return out

@app.put("/task/<int:pk>/")
def update(pk)
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "",204


@app.get("/task/")
def add(pk):
    task_data = request.json
    task.insert(task_data,pk)
    return "",204

@app.delete("/task/<int:pk>/")
def delete_by_id(pk):
    task.delete_by_id(pk)
    return "",204

@app.get("/task/<int:pk>/")
def select_by_id(pk):
    task_delete = request.json
    return "",204
    