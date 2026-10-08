from fastapi import FastAPI
from todo import todo_router

app = FastAPI(
    title="Практическая работа №5 — CRUD и обработка ошибок",
    description="Выполнила: Тимербаева Анастасия"
)

app.include_router(todo_router)

@app.get("/")
async def root() -> dict:
    return {
        "message": "Практическая работа №5 по FastAPI",
        "developer": "Тимербаева Анастасия"
    }
