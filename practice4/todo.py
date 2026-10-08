from fastapi import APIRouter, Path
from model import Todo, TodoItem

todo_router = APIRouter()

todo_list = []

# 1. Добавление задачи (POST)
@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"сообщение": f"Дело с ID {todo.id} успешно добавлено в список!"}

# 2. Получение всех задач (GET)
@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {"список_дел": todo_list}

# 3. Получение одной задачи по ID (GET)
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="ID задачи для поиска")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"дело": todo}
    return {"ошибка": f"Дело с номером {todo_id} не найдено в списке."}

# 4. Обновление задачи по ID (PUT)
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="ID задачи для обновления")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"сообщение": "Дело успешно обновлено!"}
    return {"ошибка": f"Дело с номером {todo_id} не найдено."}

# 5. УДАЛЕНИЕ ОДНОЙ ЗАДАЧИ ПО ID (DELETE)
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int = Path(..., title="ID задачи для удаления")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"сообщение": f"Дело с ID {todo_id} успешно удалено!"}
    return {"ошибка": f"Дело с номером {todo_id} не найдено."}

# 6. УДАЛЕНИЕ СРАЗУ ВСЕХ ЗАДАЧ (DELETE)
@todo_router.delete("/todo")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {"сообщение": "Все дела успешно удалены из списка!"}
