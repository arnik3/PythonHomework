"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""
from multiprocessing import Process, Value

def sum_even(result, start, end):
    total = 0
    for i in range(start, end+1):
        if i % 2 == 0:
            total += i
    result.value = total

def sum_odd(result, start, end):
    total = 0
    for i in range(start, end+1):
        if i % 2 != 0:
            total += i
    result.value = total

if __name__ == "__main__":
    start = 1
    end = 1000000
    result_even = Value('i', 0)
    result_odd = Value('i', 0)

    p1 = Process(target=sum_even, args=(result_even, start, end))
    p2 = Process(target=sum_odd, args=(result_odd, start, end))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Сумма четных чисел: ", result_even.value)
    print("Сумма нечетных чисел: ", result_odd.value)