from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

# Временное хранилище в памяти
todo_list = []

# 1. Создание задачи (POST) со статусом 201
@todo_router.post("/todo", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Задача успешно добавлена (Разработчик: Тимербаева Анастасия)"
    }

# 2. Получение всех задач (GET) с использованием response_model
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }

# 3. Получение одной задачи по ID (GET)
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(..., title="ID задачи для получения")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с указанным ID не найдена (Разработчик: Тимербаева Анастасия)"
    )

# 4. Обновление задачи (PUT)
@todo_router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="ID задачи для обновления")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Задача успешно обновлена (Разработчик: Тимербаева Анастасия)"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с указанным ID не найдена (Разработчик: Тимербаева Анастасия)"
    )

# 5. Удаление одной задачи (DELETE)
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(
    todo_id: int = Path(..., title="ID задачи для удаления")
) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Задача успешно удалена (Разработчик: Тимербаева Анастасия)"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с указанным ID не найдена (Разработчик: Тимербаева Анастасия)"
    )

# 6. Удаление всех задач (DELETE)
@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Все задачи успешно удалены (Разработчик: Тимербаева Анастасия)"
    }
