login = input()
valid = "=?*^$№@_"
response = ""
for i in login:
    for j in valid:
        if i == j:
            response += j

print(response)