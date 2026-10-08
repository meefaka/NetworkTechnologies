from fastapi import FastAPI
from todo import todo_router

app = FastAPI(title="Todo App with Jinja2 Templates")

app.include_router(todo_router)
