from fastapi import APIRouter, HTTPException, status, Body, Path
from models.events import Event, EventUpdate
from typing import List

event_router = APIRouter(tags=["Events"])

events: List[Event] = []

# 1. Получение всех событий
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events

# 2. Получение события по ID (с проверкой на 404)
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int = Path(..., gt=0)) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Событие с ID={id} не найдено"
    )

# 3. Создание события (с проверкой на дубликат ID -> 409 Conflict)
@event_router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_event(body: Event = Body(...)) -> dict:
    # ПРОВЕРКА НА ДУБЛИКАТ:
    for event in events:
        if event.id == body.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Событие с ID={body.id} уже существует! Используйте другой идентификатор."
            )
    
    events.append(body)
    return {
        "message": "Событие успешно создано",
        "event_id": body.id
    }

# 4. Обновление события (PUT) с проверкой на 404
@event_router.put("/{id}")
async def update_event(
    data: EventUpdate,
    id: int = Path(..., gt=0)
) -> dict:
    for event in events:
        if event.id == id:
            if data.title is not None:
                event.title = data.title
            if data.image is not None:
                event.image = data.image
            if data.description is not None:
                event.description = data.description
            if data.tags is not None:
                event.tags = data.tags
            if data.location is not None:
                event.location = data.location
            return {"message": f"Событие с ID={id} успешно обновлено"}
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Невозможно обновить: событие с ID={id} отсутствует"
    )

# 5. Удаление события по ID (с проверкой на 404)
@event_router.delete("/{id}")
async def delete_event(id: int = Path(..., gt=0)) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": f"Событие с ID={id} успешно удалено"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Событие с ID={id} не найдено для удаления"
    )

# 6. Удаление всех событий (с проверкой на пустой список)
@event_router.delete("/")
async def delete_all_events() -> dict:
    if not events:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Список событий уже пуст, нечего удалять"
        )
    events.clear()
    return {"message": "Все события успешно удалены"}
