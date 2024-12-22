# Цель: научится писать необходимую валидацию для вводимых данных при помощи классов Path и Annotated.

from fastapi import FastAPI, Query, Path
from typing import Annotated

# Создаем приложение FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/", summary="Get Main Page")
async def read_main() -> str:
    return "Главная страница"

# Маршрут к странице администратора
@app.get("/user/admin", summary="Get Admin Page")
async def read_admin() -> str:
    return "Вы вошли как администратор"

# Маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}", summary="Get User Number")
async def read_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]) -> str:
    return f"Вы вошли как пользователь № {user_id}"

# Маршрут к страницам пользователей с передачей имени и возраста в пути
@app.get("/user/{username}/{age}", summary="Get User Info")
async def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]
) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
