num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))

if num1 < num2: #Сравниваем числа
    print(num1,"меньше числа" , num2)
elif num1 == num2:
    print("Числа равны")    
else:
    print(num2,"меньше числа" , num1)    