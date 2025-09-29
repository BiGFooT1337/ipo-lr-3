# Задаем правильный пароль
correct_password = "qwerty123"

# Получаем пароль от пользователя
user_password = input("Введите пароль: ")

# Проверяем пароль с помощью условного оператора
if user_password == correct_password:
    print("**Доступ разрешен**")
else:
    print("**Доступ запрещен**")
