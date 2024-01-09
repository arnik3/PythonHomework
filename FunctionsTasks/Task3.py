"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""
def check_admission(score):
    if score > 50:
        return True
    else:
        return False

def main():
    num_students = int(input("Введите количество учеников: "))

    for i in range(num_students):
        score = int(input(f"Введите балл за финальный тест для ученика {i+1}: "))
        admission_status = check_admission(score)
        if admission_status:
            print("Допущен к зачету (True)")
        else:
            print("Вы отчислены (False)")

if __name__ == "__main__":
    main()
