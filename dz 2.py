class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def info(self):
        print(' Я ',self.species,' Мене звуть ',self.name,' мені ',self.age,' роки.')


class Sobaka(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Собака")


class Kit(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Кіт")


sobaka = Sobaka("Рекс", 3)
kit = Kit("Мурчик", 2)

sobaka.info()
kit.info()


class TransportnyiZasib:
    def __init__(self, speed):
        self.speed = speed

    def peremishchennia(self):
        print(' Я рухаюся зі швидкістю ',self.speed, ' км/год. ')


class Avto(TransportnyiZasib):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def info(self):
        print(' Це автомобіль марки ',self.brand,' що рухається зі швидкістю ',self.speed,' км/год ')


class Velosyped(TransportnyiZasib):
    def __init__(self, speed, type):
        super().__init__(speed)
        self.type = type

    def info(self):
        print( 'Це велосипед типу ',self.type,' що рухається зі швидкістю ',self.speed,' км/год.')


avto = Avto(120, "Toyota")
velosyped = Velosyped(25, "Гірський")

avto.info()
velosyped.info()


