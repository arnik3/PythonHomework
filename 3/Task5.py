number = input()
s = sum(map(int,str(number)))

if s % 3 == 0 and int(number[-1]) % 2 == 0:
    print("Делится")
else:
    print("Не делится")