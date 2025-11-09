a = float (input("first number:"))
operation = input("Введіть дію (+, -, *, /): ")
b = float (input("second number:"))

if operation == '+':
    result = a + b
    print("Результат:", result)

elif operation == '-':
    result = a - b
    print("Результат:", result)

elif operation == '*':
    result = a * b
    print("Результат:", result)

elif operation == '/':
    if b != 0:
        result = a / b
        print("Результат:", result)
    else:
        print("Помилка: дільник не може дорівнювати 0!")
else:
    print("Помилка: невідома операція!")

