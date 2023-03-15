professors = []

a = input('Записать нового учителя(да/нет)').lower()

while a != 'нет':
    professor = []
    if a == 'да':
        professor.append(input('Фамилия преподавателя: '))
        professor.append(input('Должность: '))
        professor.append(input('Количество студентов во всех группах(например: 12,8,10): '))
        professors.append(professor)
    print(professors)
    a = input('Записать нового учителя(да/нет)').lower()

