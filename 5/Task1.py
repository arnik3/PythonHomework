value = input()
games = []

while value != '0':
    if value in games:
        print('Это игра уже есть')
    else:
        games.append(value)

    value = input()