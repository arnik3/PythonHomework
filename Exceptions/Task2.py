"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, то есть соединение, строк.
В остальных случаях введенные числа суммируются.
"""
value1 = input("Введите первое значение: ")
value2 = input("Введите второе значение: ")

if value1.isnumeric() and value2.isnumeric():
    result = int(value1) + int(value2)
    print("Сумма введенных чисел:", result)
else:
    result = value1 + value2
    print("Конкатенация введенных значений:", result)
