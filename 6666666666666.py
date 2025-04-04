import random as r
class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health =  health

    def take_damage(self, amount):
        self.__health = self.__health - amount

    def get_info(self):
        return self.__name,self.__health

    def attack(self,num):
        pass
    def isLife(self):
        return self.__health > 0
class Warrior(Character):
    def __init__(self,name, health=r.randint(75,100)):
        super.__init__(name, health)
    def attack(self, num):
        print('Атака мечем',self.get_info())
        num.take_damage(r.randint(1,20))
class Mage(Character):
    def __init__(self,name, health=r.randint(45,75)):
        super.__init__(name, health)
    def attack(self, num):
        print('Атака магією',self.get_info())
        num.take_damage(r.randint(5,30))


class LibraryItem:
    def __init__(self, title, author, item_id):
        self._title = title
        self._author = author
        self._item_id = item_id

    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self._pages = pages

    def display_info(self):
        print('Книга:',self._title,'Автор:',self._author,'Сторінки:',self._pages)


class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self._issue_number = issue_number

    def display_info(self):
        print('Журнал:',self._title,'Автор:',self._author,'Номер випуску:',self._issue_number)


class Audiobook(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self._duration = duration

    def display_info(self):
        print('Аудіокнига:',self._title,'Автор:',self._author,'Тривалість:',self._duration,'хвилин')


library_items = [
    Book("Війна і мир", "Лев Толстой", 1, 1225),
    Magazine("Наука і життя", "Редакція", 2, 34),
    Audiobook("1984", "Джордж Орвелл", 3, 780)
                ]

for item in library_items:
    item.display_info()
