class Car:
    count = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.count += 1

    def get_info(self):
        return "[" + str(self.year) + "] " + self.make + " " + self.model


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return "Заробітна плата " + self.name + ": " + str(self.salary)


# Перевірка класу Car
auto1 = Car("BMW", "X5", 2022)
print(auto1.get_info())

auto2 = Car("Audi", "A6", 2020)
print(auto2.get_info())
print("Кількість створених авто: " + str(Car.count))

# Перевірка класу Employee
emp1 = Employee("Іван Петренко", "Інженер", 25000)
print(emp1.get_salary_info())

emp2 = Employee("Марія Коваленко", "Менеджер", 30000)
print(emp2.get_salary_info())
