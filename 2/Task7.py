name = input()
a = ""

a += name[:name.find(" ")] + " "

name = name[name.find(" ") + 1:]
a += name[0] + "."

name = name[name.find(" ") + 1:]
a += name[0] + "."

print(a)