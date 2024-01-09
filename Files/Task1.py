"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""
with open('genius.txt', 'w') as file:
    file.write("Я гений и стараюсь учить питон")

with open('genius.txt', 'r') as file:
    content = file.read()
    print(content[:7])
