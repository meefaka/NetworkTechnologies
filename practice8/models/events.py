from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional, List

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(default=[], sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "title": "Презентация книги по FastAPI",
                "image": "https://example.com/poster.png",
                "description": "Обсуждение практических примеров и архитектуры веб-приложений.",
                "tags": ["программирование", "fastapi", "python"],
                "location": "Яндекс Телемост"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Обновленная презентация по FastAPI",
                "location": "Главный лекторий"
            }
        }
