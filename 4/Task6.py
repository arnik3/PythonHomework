cost = int(input())

while cost != 0:
    if cost % 2 == 0:
        while cost % 2 == 0:
            cost /= 2
    else:
        cost = round(cost * 0.85, 2)

    print(f"К оплате: {cost}")
    cost = int(input())