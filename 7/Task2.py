"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False и изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]
result = []
printSet = set()

for i in testList:
    if type(i) == list or type(i) == set or type(i) == dict:
        result.append(i)
    else:
        printSet.add(i)

print(printSet, result, bool(not result))
