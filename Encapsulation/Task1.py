"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""
class BankAccount:
    def __init__(self, name, balance, passport):
        self._name = name
        self.__balance = balance
        self.__passport = passport
        self.password = "qwerty"  # простой пароль для примера

    def get_balance(self):
        return self.__balance

    def get_passport(self, password):
        if password == self.password:
            return self.__passport
        else:
            return "Access denied"

    def change_passport(self, new_passport, password):
        if password == self.password:
            self.__passport = new_passport
            return "Passport number has been changed"
        else:
            return "Access denied"

    def change_balance(self, amount, password):
        if password == self.password:
            new_balance = self.__balance + amount
            if new_balance < 0:
                return "Operation denied, balance can't be negative"
            else:
                self.__balance = new_balance
                return "Balance has been changed"
        else:
            return "Access denied"

    def delete_passport_data(self, password):
        if password == self.password:
            del self.__passport
            return "Passport data has been deleted"
        else:
            return "Access denied"

# Пример использования:
account = BankAccount("John Doe", 1000, "AB1234567")
print(account.get_balance())
print(account.get_passport("password"))
print(account.get_passport("qwerty"))
print(account.change_passport("BC7654321", "password"))
print(account.change_passport("BC7654321", "qwerty"))
print(account.change_balance(-1200, "qwerty"))
print(account.change_balance(-200, "qwerty"))
print(account.delete_passport_data("password"))
print(account.delete_passport_data("qwerty"))
