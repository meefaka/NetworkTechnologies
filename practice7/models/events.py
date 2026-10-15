from pydantic import BaseModel, Field
from typing import List, Optional

class Event(BaseModel):
    id: int = Field(..., gt=0, description="ID события должен быть больше 0")
    title: str = Field(..., min_length=2, description="Название не должно быть пустым")
    image: str = Field(..., description="Ссылка на баннер")
    description: str = Field(..., min_length=5, description="Описание минимум 5 символов")
    tags: List[str] = Field(..., min_items=1, description="Минимум один тег")
    location: str = Field(..., min_length=2, description="Место проведения")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "Презентация и обсуждение новой книги по FastAPI.",
                "tags": ["python", "fastapi", "book"],
                "location": "Google Meet"
            }
        }

# Модель для частичного обновления (все поля необязательные)
class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
