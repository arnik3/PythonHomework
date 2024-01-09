"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def calculate_bmi(weight, height):
    return weight / (height * height)

def process_bmi(bmi):
    if bmi < 18.5:
        print("Недостаточный вес")
    elif bmi >= 18.5 and bmi <= 25:
        print("ИМТ в норме")
    else:
        print("Избыточный вес")

def main():
    weight = float(input("Введите ваш вес в килограммах: "))
    height = float(input("Введите ваш рост в метрах: "))

    bmi = calculate_bmi(weight, height)
    print(f"Ваш ИМТ: {bmi:.2f}")
    process_bmi(bmi)

if __name__ == "__main__":
    main()
