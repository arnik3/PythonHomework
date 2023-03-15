string = input().split()

good_rating = string.count('5')

print(good_rating * 100 / len(string))
