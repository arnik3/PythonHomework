"""
Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и сохранять их в таком
виде в новом файле. Имя исходного файла необходимо запросить у пользователя, так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего
должен идти текст строки из исходного файла.
"""
input_file_name = input("Введите имя исходного файла: ")
output_file_name = input("Введите имя целевого файла: ")

with open(input_file_name, 'r') as input_file:

    lines = input_file.readlines()

with open(output_file_name, 'w') as output_file:
    for i, line in enumerate(lines, 1):
        output_file.write(f"{i}: {line}")

print("Содержимое исходного файла было успешно записано в новый файл с порядковыми номерами.")
