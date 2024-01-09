"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open('not_genius.txt', 'w') as file:
    file.write("но у меня не получается")

with open('genius.txt', 'r') as file1, open('not_genius.txt', 'r') as file2, open('combined_file.txt', 'w') as file3:
    content1 = file1.read()
    content2 = file2.read()
    file3.write(content1 + "\n" + content2)