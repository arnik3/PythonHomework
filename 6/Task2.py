"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
numbers = "0139412831055230677798"
listdictionary ={}

for i in range(0, 10):
    listdictionary[i] = list(numbers).count(str(i))
print(listdictionary)