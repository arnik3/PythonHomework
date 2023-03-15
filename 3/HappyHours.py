
a = int(input("сумма к оплате: "))
b = int(input("Укажите час: "))

if 8 <= b <= 22:
    if 20 <= b <= 22:
        print(a//4)
    if 10 <= b <= 12:
        print(a//2)
else:
    print("Магазин закрыт")