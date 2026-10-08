from pydantic import BaseModel

# Класс для обновления текста задачи (его не хватало)
class TodoItem(BaseModel):
    item: str

# Класс для создания задачи с ID
class Todo(BaseModel):
    id: int
    item: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "item": "Сделать практическую работу №4"
            }
        }
    }