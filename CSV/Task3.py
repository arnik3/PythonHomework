"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""
dict_scv = [['infa', 'Olga Naumova', 20],
               ['Math', 'Rustem Raimanovich', 459],
               ['subjects', 'all', 15],
               ['Pyton', 'Oleg Yurievich ', 20]]

import csv

with open('arnik.csv', 'w') as f:
    writer = csv.writer(f)
    for i in dict_scv:
        writer.writerow(i)