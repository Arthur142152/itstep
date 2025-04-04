#ПОЛІМОРФІЗМ
#class Animal:
    #def sound(self):
        #pass
#class Cat(Animal):
    #def sound(self):
        #return 'Кішка-мявчить'
#class Dog(Animal):
    #def sound(self):
        #return 'Собака-гавкає'
#class Bird(Animal):
    #def sound(self):
        #return 'Птичка-чірікає'
#def speak(anim):
    #print(anim.sound())

#a1=Cat()
#a2=Dog()
#a3=Bird()
#speak(a1)
#speak(a2)
#speak(a3)
#class Pay:
    #def system(self,money):
        #pass
#class Cash(Pay):
    #def system(self,money):
        #return ' Оплата '+str(money)+' була здійснена через готівку '
#class Credit(Pay):
    #def system(self,money):
        #return ' Оплата ' +str(money)+ ' була здійснена через кредитну картку '
#class Online(Pay):
    #def system(self,money):
        #return ' Оплата ' +str(money)+ ' була здійснена через онлайн систему '
#payList=[Cash(),Credit(),Online()]
#for k in payList:
    #print(k.system( 125 ))
#Інкапсуляція



#class Dog:
    #def __init__(self,name):
        #self.name=name
#dog1=Dog('Барбос')
#print(dog1.name)



#class Dog:
    #def __init__(self,name):
        #self.__age=1
    #def InfoAge(self):
        #return self.__age
#dog1=Dog('Барбос')
#print(dog1.InfoAge())
#print(dog1.__age)

#class Dog:
    #def __init__(self,name):
        #self._breed='Лабрадор'
#class Puppy(Dog):
    #def info(self):
        #return'Цуценя породи '+self._breed
#dog1=Puppy('Барбос')
#print(dog1.info())

#class Person():
    #def __init__(self,name,age,salary):
        #self.name=name
        #self._age=age
        #self.__salary=salary
    #def info(self):
        #print('Вітаю,мене звати',self.name)
        #self._infoAge()
        #self.__infoSalary()


    #def _infoAge(self):
        #print('Мій вік',self._age)
    #def __infoSalary(self):
        #print('Моя зп',self.__salary)
#class Employee(Person):
    #def __init__(self,name,age,salary,pos):
        #super().__init__(name,age,salary)
        #self.pos=pos
    #def infoEmp(self):
        #print(self.name,'займає посаду',self.pos)
        #self._infoAge()
        #self.__infoSalary()
        #print('вік:',self._age,)
        #print('зп:', self.__salary)
#p1=Person('Олександр',25,58000)
#e1=Employee('Олена',32,40000,'Дизайнер')
#print(p1.name)
#p1.info()
#print(e1.name)
#e1.infoEmp()
#print(e1._Person__salary)

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














