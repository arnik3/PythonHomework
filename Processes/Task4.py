"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""
import threading
import time

def check_subscription_expiry():
    time.sleep(10)
    print("Ваша подписка закончилась.")
    exit()

subscription_thread = threading.Thread(target=check_subscription_expiry)
subscription_thread.start()


