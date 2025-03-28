#class Human:
    #count=0
    #def __init__(self,name="Petya"):
        #self.name=name
        #Human.count+=1
#class Auto:
    #def __init__(self,brand):
        #self.brand=brand
        #self.passenger=[]
    #def add(self,*pas):#необмежена кількість аргументів
        #for p in pas:
            #self.passenger.append(p)
    #def info(self):
        #if self.passenger==[]:
            #print("Маршрутка бренду",self.brand,"Немає пасажирів")
        #else:
            #print("Маршрутка бренду", self.brand, "має пасажирів")
            #for p in self.passenger:
               # print(p.name)
#pas1=Human()
#pas2=Human("Tanya")
#pas3=Human("Sasha")
#car=Auto('Богдан')
#car.add(pas1)
#car.add(pas2)
#car.add(pas3)
#car.add(pas1,pas2,pas3)
#car.info()
#print('Кількість пасажирів:',Human.count)
#class Human:
    #def __init__(self,name,age,height,national,city,weight):
        #self.name=name
        #self.age=age
        #self.height=height
        #self.national=national
        #self.city=city
        #self.weight=weight
    #def __str__(self):
        #return 'Вітаю! Я '+str(self.name)+' з міста '+str(self.city)+' мені '+str(self.age)+' мій зріст '+str(self.height)+' моя вага '+str(self.weight)+' я '+str(self.national)
#class Pupil(Human):
    #def __init__(self,name,age,height,national,city,weight,school,clas):
        #super().__init__(name,age,height,national,city,weight)
        #self.school=school
        #self.clas=clas
    #def __str__(self):
        #return super().__str__()+' навчаюсь в школі під номером '+str(self.school)+' в класі '+str(self.clas)
#class Worker(Human):
    #def __init__(self, name, age, height, national, city, weight,salary,kids):
        #super().__init__(name, age, height, national, city, weight)
        #self.salary = salary
        #self.kids=kids
    #def __str__(self):
        #return super().__str__()+' моя заробітня плата '+str(self.salary)+' в мене '+str(self.kids)+' дітей '

#woman=Human('Марина',20,170,'Українка','Запоріжжя',55)
#print(woman)
#p=Pupil('Саша',11,137,'українець','Дніпро', 34,42, 6)
#print(str(p))
#w=Worker("Михайло",35,187,"Поляк",'Київ',72,11000,4)
#print(str(w))
#class Computer:
    #def __init__(self):
        #super().__init__()
        #self.model='Apple'
        #self.memory=256
#class Display:
    #def __init__(self):
        #super().__init__()
        #self.resol='4k'
#class Smartphone(Computer,Display):
    #def info(self):
        #print('смартфон моделі',self.model,"має параметри,об'єм пам'яті",self.memory,"розширення екрану",self.resol)
#tel=Smartphone()
#tel.info()


class Devise:
    def __init__(self):
        super().__init__()
        self.name = 'Xiaomi'


class Display:
    def __init__(self):
        super().__init__()
        self.weight = '241 gramm'


class Tablet(Devise, Display):
    def info(self):
        print( self.name, "важить", self.weight)


descripition = Tablet()
descripition.info()