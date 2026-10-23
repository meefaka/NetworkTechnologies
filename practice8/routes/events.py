from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select, Session
from database.connection import get_session
from models.events import Event, EventUpdate
from typing import List

event_router = APIRouter(tags=["События"])

# 1. Создание события
@event_router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_event(new_event: Event, session: Session = Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message": "Событие успешно создано",
        "id": new_event.id
    }

# 2. Получение всех событий
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session: Session = Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

# 3. Получение события по ID
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session: Session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Событие с указанным ID не найдено"
    )

# 4. Редактирование события
@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session: Session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Событие с указанным ID не найдено"
        )
    event_data = new_data.model_dump(exclude_unset=True) if hasattr(new_data, "model_dump") else new_data.dict(exclude_unset=True)
    for key, value in event_data.items():
        setattr(event, key, value)
        
    session.add(event)
    session.commit()
    session.refresh(event)
    return event

# 5. Удаление события
@event_router.delete("/delete/{id}")
async def delete_event(id: int, session: Session = Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Событие с указанным ID не найдено"
        )
    session.delete(event)
    session.commit()
    return {
        "message": "Событие успешно удалено"
    }
