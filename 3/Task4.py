category = input("Ввелите категорию ").lower()
if category == "продукты":
    price = int(input("Укажите цену"))
    if  price < 100:
        print("Попробуйте наши напитки!")
    if 100 < price < 500:
        print("Как насчёт яблочного сока?")
    if price > 500:
        print("Попробуйте экзотические фрукты!")
else:
    print("Загляните в товары для дома!")