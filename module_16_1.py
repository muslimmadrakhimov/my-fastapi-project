from fastapi import FastAPI, Query

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
async def read_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"

# Маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user", summary="Get User Info")
async def read_user_info(username: str, age: int) -> str: 
     return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

