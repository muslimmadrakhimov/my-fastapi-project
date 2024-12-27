# Цель: научиться описывать и использовать Pydantic модель.
#
# Задача "Модель пользователя":



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Инициализация приложения FastAPI
app = FastAPI()

# Список пользователей, где мы будем хранить данные.
users = []

# Определяем модель пользователя, которая будет описывать структуру данных.
# Наследуемся от BaseModel для использования Pydantic.
class User(BaseModel):
    id: int  # Идентификатор пользователя
    username: str  # Имя пользователя
    age: int  # Возраст пользователя

# 1. GET запрос для получения списка всех пользователей
@app.get("/users", response_model=List[User])
async def get_users():
    # Возвращаем список пользователей
    return users

# 2. POST запрос для добавления нового пользователя
@app.post("/user/", response_model=User)
async def create_user(user: User):
    # Если список пользователей пустой, присваиваем id = 1
    # В противном случае id будет на 1 больше, чем у последнего пользователя
    user_id = users[-1].id + 1 if users else 1

    # Создаем нового пользователя
    new_user = User(id=user_id, username=user.username, age=user.age)

    # Добавляем пользователя в список
    users.append(new_user)

    # Возвращаем созданного пользователя
    return new_user

# 3. PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    # Ищем пользователя по id
    for existing_user in users:
        if existing_user.id == user_id:
            # Если нашли пользователя, обновляем его данные
            existing_user.username = user.username
            existing_user.age = user.age
            return existing_user

    # Если пользователя с таким id нет, выбрасываем ошибку
    raise HTTPException(status_code=404, detail="User was not found")

# 4. DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    # Ищем пользователя по id
    for user in users:
        if user.id == user_id:
            # Если нашли пользователя, удаляем его из списка
            users.remove(user)
            return user

    # Если пользователя с таким id нет, выбрасываем ошибку
    raise HTTPException(status_code=404, detail="User was not found")
