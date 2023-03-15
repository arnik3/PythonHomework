numbers = input()
numbers = [int(x) for x in numbers.split()]

if len(numbers) == 1:
    print('Нет')
elif sorted(numbers) == numbers:
    print('Да')
else:
    print('Нет')
