#Вводим день и месяц
day = int(input("Введите день:"))
month = int(input("Введите месяц:"))
#Проверяем номер месяца и вывовид пору года
if  3 <= month <= 5:
    print(day, "число", month, "месяц", " - Весна")
elif 6 <= month <= 8:
    print("Лето")
elif 9 <= month <= 11:
    print("Осень")
else:
    print("Зима")        

