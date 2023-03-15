a = [5,3,2,4]
quantity = len(a)
print(quantity)
c = 0

for i in a:
    if 3<=i<=5:
        c += 1

print(c/quantity*100)