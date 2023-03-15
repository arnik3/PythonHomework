string = "ААААBBBCCF"
result = ""

for i in set(string):
    number = string.count(string[0])
    result += str(number)
    result += string[0]
    string = [j for j in string if j != string[0]]

print(result)