def login(username, password):
    try:
        assert username == "admin" and password == "12345"
        print("Вхід виконано успішно")
    except AssertionError:
        print("Невірне ім'я користувача або пароль")


login("admin", "12345")
login("user", "123")