import random as r


class Student:
    def __init__(self, name='Яна'):
        self.name = name
        self.happy = r.randint(50, 100)
        self.prog = r.randint(1, 12)
        self.isStudy = True

    def study(self):
        print('час на навчання')
        self.happy -= r.randint(10, 50)
        self.prog += r.randint(1, 5)

    def chill(self):
        print('час для відпочинку')
        self.happy -= r.randint(10, 50)
        self.prog += r.randint(1, 5)

    def sleep(self):
        print('час для сну')
        self.happy -= r.randint(1, 20)

    def isLife(self):
        if self.prog > 6:
             print('все добре з навчанням', end='')
             if 7 <= self.prog < 10:
                print('все добре з навчанням, але можно краще')
            else:
                print('Відміно вчишся!!!!!!!!!')
        elif 4 <= self.prog <= 6:
            print('ти погано вчишся')

        else:
            print('ти найгірший учень')
            self.isStudy=False

    def everyday(self):
        print('рівень щастя', self.happy)
        print('прогрес навчання', self.prog)


    def studyLife(self, day):
        day = '\nДень№' + str(day)
        print('day')
        res = r.randint(1, 3)

        if res == 1:
            self.chill()
        elif res == 2:
            self.sleep()
        else:
            self.study()

        self.everyday()
        self.isLife()
st1=Student('Яна')
for k in range(1,8):
    print('Життя студента:', st1.name)
    if st1.isStudy==False:
        break
    st1.studyLife(k)
st2=Student('Саша')
print('Життя студента:', st2.name)
for k in range(1,8):
    if st2.isStudy == False:
        break
    st2.studyLife(k)
# st1=Student()
 # print(st1.prog)