"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.__rank = None

    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        self.__rank = new_rank

    def del_rank(self):
        self.__rank = None

hero = Hero("Arthur", 100)


hero.set_rank("Победитель арены")
print(hero.get_rank())

hero.del_rank()
print(hero.get_rank())
