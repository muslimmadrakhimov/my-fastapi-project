from fastapi import FastAPI, Query

# Создаем приложение FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/", summary="Get Main Page")
def read_main():
    return {"message": "Главная страница"}

# Маршрут к странице администратора
@app.get("/user/admin", summary="Get Admin Page")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}", summary="Get User Number")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user", summary="Get User Info")
def read_user_info(username: str = Query(..., description="Имя пользователя"),
                   age: int = Query(..., description="Возраст пользователя")):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

