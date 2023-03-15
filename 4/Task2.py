import random
inp = input()
while inp != "off":
    win = False
    rightValue = random.randint(0, 10)
    if inp == "game":
        for i in range(3):
            print("Введите сисло от 0 до 10")
            number = int(input())
            if i == rightValue:
                win = True
                break
            else:
                print("Неправильно")

            if win == True:
                print("Вы выграли билет на концерт")
            else:
                (print("Вы проиграли"))
    inp = input()
