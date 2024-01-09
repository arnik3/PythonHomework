"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
import multiprocessing

def convert_currency(money, channel):
    rate = 75
    result = money / rate
    channel.send(result)

if __name__ == '__main__':
    channel = multiprocessing.Pipe()

    amounts = [1000, 2000, 5000]

    for amount in amounts:
        p = multiprocessing.Process(target=convert_currency, args=(amount, channel[1]))
        p.start()
        p.join()
        print(f"Amount: {amount} UZS  |  Converted currency: {channel[0].recv()} USD")