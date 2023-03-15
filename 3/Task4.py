category = input("Ввелите категорию ").lower()
if category == "продукты":
    price = int(input("Укажите цену"))
    if  price < 100:
        print("Попробуйте нашу выпечку!")
    if 100 < price < 500:
        print("Как насчёт орехов в шоколаде?")
    if price > 500:
        print("Попробуйте экзотические фрукты!")
else:
    print("Загляните в товары для дома!")