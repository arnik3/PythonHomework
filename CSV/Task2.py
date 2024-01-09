"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""
import csv
dict = {}

with open('Task1.csv') as f:
    lector = csv.lector(f, delimiter=';')
    for i in lector:
        dict[(i[0], i[1])] = {i[2] : i[3]}
    print(dict)