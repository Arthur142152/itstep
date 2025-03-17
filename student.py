import random as r

class Student:
    def __init__(self, name='Яна'):
        self.name = name
        self.happy = r.randint(50, 100)
        self.prog = r.randint(1, 12)
        self.money = r.randint(100, 500)
        self.isStudy = True

    def study(self):
        print('Час на навчання')
        self.happy -= r.randint(10, 30)
        self.prog += r.randint(1, 5)

    def chill(self):
        print('Час для відпочинку')
        if self.money >= 20:
            self.money -= 20
            self.happy += r.randint(10, 30)
        else:
            print('Немає грошей на розваги!')

    def sleep(self):
        print('Час для сну')
        self.happy += r.randint(5, 15)

    def work(self):
        print('Час на роботу')
        self.money += r.randint(50, 150)
        self.happy -= r.randint(5, 20)

    def isLife(self):
        if self.prog > 9:
            print('Відмінно вчишся!')
        elif 7 <= self.prog <= 9:
            print('Все добре з навчанням, але можна краще')
        elif 4 <= self.prog < 7:
            print('Ти погано вчишся')
        else:
            print('Ти найгірший учень!')

    def everyday(self):
        print('Рівень щастя:',self.happy)
        print('Прогрес навчання:',self.prog)
        print('Гроші:', self.money)

    def studyLife(self, day):
        print('День №',day)
        if self.money < 50:
            print('Грошей мало! Йду працювати.')
            self.work()
        elif self.happy < 30:
            print('Настрій поганий, треба відпочити.')
            self.chill()
        elif self.prog < 6:
            print('Треба більше вчитися!')
            self.study()
        else:
            self.sleep()
        self.everyday()
        self.isLife()

    def liveYear(self):
        for day in range(1, 366):
            self.studyLife(day)


student = Student()
student.liveYear()