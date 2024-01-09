"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""
def calculate_room_area(width, length, height):
    with open('room_data.txt', 'a') as file:
        area = 2 * (width * height + length * height)
        file.write(f"Room area: {area} square meters\n")

def calculate_paint_usage(area):
    with open('room_data.txt', 'a') as file:
        paint_usage = area * 5
        file.write(f"Paint usage: {paint_usage} liters\n")

width = float(input("Enter room width: "))
length = float(input("Enter room length: "))
height = float(input("Enter room height: "))

calculate_room_area(width, length, height)
calculate_paint_usage(2*(width*height + length*height))

print("Data written to file.")