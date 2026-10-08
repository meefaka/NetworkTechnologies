from pydantic import BaseModel
from typing import List

# Модель для полной задачи
class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Пример задачи от Тимербаевой Анастасии"
            }
        }

# Модель для обновления задачи (без ID)
class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Изучить модели ответов FastAPI"
            }
        }

# Модель ответа со списком задач (скрывает ID)
class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {"item": "Пример задачи 1"},
                    {"item": "Пример задачи 2"}
                ]
            }
        }
