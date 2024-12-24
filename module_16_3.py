# Цель: выработать навык работы с CRUD запросами.

# Задача "Имитация работы с БД":



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, conint

# Создаём экземпляр приложения FastAPI
app = FastAPI()

# Инициализация словаря users - это наша "база данных" на время работы приложения
users = {'1': 'Имя: Example, возраст: 18'}

# Создаём модель данных для валидации входных данных при обновлении пользователя
class UserUpdate(BaseModel):
    username: constr(min_length=1, max_length=50)  # Имя пользователя от 1 до 50 символов
    age: conint(ge=0)  # Возраст должен быть неотрицательным целым числом

# GET запрос для получения всех пользователей
@app.get("/users")
def get_users():
    """
    Возвращает весь словарь пользователей.
    """
    return users

# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
def post_user(username: str, age: int):
    """
    Добавляет нового пользователя в словарь users.
    Параметры:
        - username: Имя пользователя (строка длиной от 1 до 50 символов)
        - age: Возраст пользователя (целое число >= 0)
    """
    # Проверяем длину имени пользователя
    if len(username) < 1 or len(username) > 50:
        raise HTTPException(status_code=400, detail="Username must be between 1 and 50 characters.")
    # Проверяем, что возраст неотрицательный
    if age < 0:
        raise HTTPException(status_code=400, detail="Age must be a non-negative integer.")

    # Находим следующий доступный ID пользователя
    new_id = str(max(map(int, users.keys())) + 1)
    # Добавляем запись в словарь
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

# PUT запрос для обновления пользователя
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    """
    Обновляет данные существующего пользователя по его ID.
    Параметры:
        - user_id: ID пользователя (ключ в словаре users)
        - username: Новое имя пользователя (строка длиной от 1 до 50 символов)
        - age: Новый возраст пользователя (целое число >= 0)
    """
    # Проверяем, существует ли пользователь с таким ID
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    # Проверяем длину имени пользователя
    if len(username) < 1 or len(username) > 50:
        raise HTTPException(status_code=400, detail="Username must be between 1 and 50 characters.")
    # Проверяем, что возраст неотрицательный
    if age < 0:
        raise HTTPException(status_code=400, detail="Age must be a non-negative integer.")

    # Обновляем запись в словаре
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    """
    Удаляет пользователя по его ID.
    Параметры:
        - user_id: ID пользователя (ключ в словаре users)
    """
    # Проверяем, существует ли пользователь с таким ID
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    # Удаляем запись из словаря
    del users[user_id]
    return f"User {user_id} has been deleted"
