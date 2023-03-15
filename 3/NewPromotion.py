print("Введите цены товаров.\nПример: 2500,45,87,5")

prices = input().split(",")

sum = sum(list(map(int, prices)))

if len(prices) == 3:
    if int(prices[0]) < int(prices[1]) <int(prices[2]):
        print(f"Акция {sum/2}")

    if int(prices[0]) > int(prices[1]) > int(prices[2]):
        print(f"Акция {sum/2}")
else:
    print(sum)
