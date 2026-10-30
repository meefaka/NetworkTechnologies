from beanie import Document
from typing import Optional, List
from pydantic import BaseModel

class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Settings:
        name = "events"

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Хакатон по веб-разработке",
                "image": "https://example.com/poster.png",
                "description": "Практическое создание асинхронных веб-сервисов.",
                "tags": ["python", "fastapi", "mongodb"],
                "location": "Главный корпус, ауд. 305"
            }
        }

class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Хакатон по веб-разработке (Финал)",
                "location": "Актовый зал"
            }
        }
