from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(tags=["Пользователи"])
users_db = {}

# Регистрация
@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def sign_new_user(data: User) -> dict:
    if data.email in users_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким адресом электронной почты уже существует"
        )
    users_db[data.email] = data
    return {"message": "Пользователь успешно зарегистрирован"}

# Вход
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь с таким email не найден"
        )
    if users_db[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Неверный пароль"
        )
    return {"message": "Успешный вход в систему"}
