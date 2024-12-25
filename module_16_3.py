# Цель: выработать навык работы с CRUD запросами.

# Задача "Имитация работы с БД":


from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field, conint
from typing import Annotated

# Создаём экземпляр приложения FastAPI
app = FastAPI()

# Инициализация словаря users - это наша "база данных" на время работы приложения
users = {'1': 'Имя: Example, возраст: 18'}

# GET запрос для получения всех пользователей
@app.get("/users")
async def get_users():
    """
    Возвращает весь словарь пользователей.
    """
    return users

# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
async def post_user(
    username: Annotated[
        str, Field(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
    ],
    age: Annotated[
        int, Field(ge=18, le=120, description="Enter age", example=24)
    ]
):
    """
    Добавляет нового пользователя в словарь users.
    Параметры:
        - username: Имя пользователя (строка длиной от 5 до 20 символов)
        - age: Возраст пользователя (целое число >= 18 и <= 120)
    """
    # Находим следующий доступный ID пользователя
    new_id = str(max(map(int, users.keys())) + 1)
    # Добавляем запись в словарь
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

# PUT запрос для обновления пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[
        int, Field(ge=1, le=100, description="Enter User ID", example=1)
    ],
    username: Annotated[
        str, Field(min_length=5, max_length=20, description="Enter username", example="UrbanProfi")
    ],
    age: Annotated[
        int, Field(ge=18, le=120, description="Enter age", example=28)
    ]
):
    """
    Обновляет данные существующего пользователя по его ID.
    Параметры:
        - user_id: ID пользователя (целое число от 1 до 100)
        - username: Новое имя пользователя (строка длиной от 5 до 20 символов)
        - age: Новый возраст пользователя (целое число >= 18 и <= 120)
    """
    # Преобразуем user_id в строку для использования в словаре
    user_id_str = str(user_id)

    # Проверяем, существует ли пользователь с таким ID
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    # Обновляем запись в словаре
    users[user_id_str] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is updated"

# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[
        int, Field(ge=1, le=100, description="Enter User ID", example=2)
    ]
):
    """
    Удаляет пользователя по его ID.
    Параметры:
        - user_id: ID пользователя (целое число от 1 до 100)
    """
    # Преобразуем user_id в строку для использования в словаре
    user_id_str = str(user_id)

    # Проверяем, существует ли пользователь с таким ID
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    # Удаляем запись из словаря
    users.pop(user_id_str)
    return f"User {user_id} has been deleted"

