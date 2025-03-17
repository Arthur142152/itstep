#class Car:
    #speed=110
    #model="BMW"
    #count=0
   # def __init__(self,speed,model):
       # self.speed=speed
        #self.m=model
        #Car.count+=1
   # def info(self):
        #print("Швидкість авто", self.speed)
        #print("Модель авто", self.m)

#auto=Car(125,"Audi")
#auto.info()
#speed=int(input(">  "))
#model=input(">  ")
#auto2=Car(speed,model)
#auto2.info()
#print(auto2.count)
#auto3=Car(325,"Porshe")
#auto3.info()
#print(auto3.count)

#auto2=Car()
#auto2.info()







#print("Модель авто",auto2.model)
#print("Швидкість авто",auto.speed)
#print("Модель авто",auto.model)







class Zm:
    def __init__(self,id=111,name='Саша',height=170):
        self.id=id
        self.name=name
        self.height=height
    def __str__(self):
        print('Інфо учасника')
        print('Номер:',str(self.id),'Имя',self.name,'Зріст:',str(self.height))
    def __bool__(self):
          return self.id!= None


p1=Zm()
#print(p1.name)
p2=Zm(112,'Даша',172)
#print(p2.height)
p1.__str__()
#print(str(p2))
print(bool(p1))
print(p2.__bool__())

