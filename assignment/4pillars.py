"""class and object"""
class nails:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
a=nails("pink","dazler")
print(a.color)
print(a.brand)
class nails:
    def __init__(self,color,cost):
        self.cost=cost
        self.color=color
    def types(self):
        print(f"the nail polish of the color is:{self.color} and the cost of the nail polish is {self.cost}")    
a=nails("matte black",79)
a.types()

"""class varibales and object variables"""
class favgod:
    godname="shiva"      """class variable"""
    def __init__(self,name,day):
        self.name=name
        self.day=day        #object variable
    def details(self):
        print(f"the name of the god is {self.godname} and very powerful on {self.day}")
    def details1(self):
        print(f"the name of the god is {self.name} and very special on  {self.day}")  
first=favgod("shivayya","monday")
first.details()
b=favgod("kumaraswamy","tuesday")
b.details1()   
a=favgod("ganesha","wednesday")
a.details1()
c=favgod("saibaba","thursday")
c.details1()
d=favgod("lakshmi devi","friday")
d.details1()
e=favgod("venkanna babu","saturday")
e.details1()

"""encapsulation"""
"""public
private .__
protected ._"""


class Account:
    def __init__(self,balance,name):
        self.__balance=balance     #private
        self.name=name          #public
    def deposit(self,amount):
        self.__balance+=amount
        return self.__balance
    def withdraw(self,amount):
        self.__balance-=amount
        return self.__balance
    def checkbalance(self):
        return self.__balance
a=Account(600,"paul")
print(a.deposit(300))
print(a.withdraw(100))
print(a.checkbalance())
print(a.name)          #it can access becoz it is public
print(a.__balance)    #cannot access becoz it is private

"""polymorphism"""

"""method overriding"""
class costliest:
    def ac(self):
        print("ac is more costlier than the cooler")
class budget:
    def ac(self):
        print("the ac gives the cool breeze")
a=costliest()
a.ac()
b=budget()
b.ac()

"""method overloading""" #in python we donot have method overloading becoz we have the similar functionality in defual paramneters and variable length arguments
class maths:
    def add(self,a=0,b=20,c=10):
        return a+b+c
a=maths()
print(a.add(1,2,3))            (#default parameters)

"""varible length arguments"""
class variable:
    def sum(self,*n):
        sum=0
        for i in n:
            sum=sum+i
        return sum
a=variable()
print(a.sum(1,2,3,4,5))

"""operator overloading"""
class Total:
    def __init__(self,amount):
        self.amount=amount
    def __add__(self,addon):
        return self.amount+addon.amount
    def __mul__(self,addon):
        return self.amount*addon.amount
    def __sub__(self,addon):
        return self.amount-addon.amount
a=Total(500)
b=Total(500)
print(a+b)
print(a*b)
print(a-b)

"""duck typing"""
class phone:
    def vivo(self):
        print("the cost if vivo phone starts from 10k")
class laptop:
    def vivo(self):
        print("the mac book cost is very higher")
def appliance(smart):
    smart.vivo()
a=phone()
appliance(a)
b=laptop()
appliance(b)

"""abstraction"""
from abc import ABC,abstractmethod
class chairs(ABC):
    @abstractmethod
    def details(self):
        pass
class values(chairs):
    def details(self):
        print("there are different kinds of chairs like folding chair,plastic chiars,wooden chair,swing chair,cup chair")
a=values()
a.details()