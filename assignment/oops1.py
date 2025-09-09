# class and object
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"{self.name} is of age {self.age}")
a=Student("himavarsha",21)
a.details()
b=Student("prasannakshi",21)
b.details()
c=Student("Jyothika",22)        
c.details()

# without method
class Car:
    def __init__(self,name):
        self.name=name
c=Car("BMW")
print(c.name)

class Food:
    type1="vegetarian"  #class variable
    def __init__(self,name):
        self.name=name    #object/instance variables
    def item(self):
        print(f"{self.name} is a {self.type1} ")
a=Food("paneer")
a.item()

class car:
    sound="uzzsuyiii"
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def display(self):
        print(f"{self.name} is of brand {self.brand} and it sound {self.sound}")
a=car("porsche",911)
a.display()

# encapsulation
class BankAccount:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        return self._balance+amount
    def withdraw(self,withdrawamount):
        return self._balance-withdrawamount
    def get_balance(self):
        return self._balance
a=BankAccount(100)
print(a.deposit(20))
print(a.withdraw(40))
print(a.get_balance())
        

class BankAccount:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
       self._balance+=amount
       return self._balance
    def withdraw(self,withdrawamount):
        self._balance-=withdrawamount
        return self._balance
    def get_balance(self):
        return self._balance
a=BankAccount(100)
print(a.deposit(20))
print(a.withdraw(40))
print(a.get_balance())


class person:
    def __init__(self,age):
        self.__age=age
    def sub(self):
        print(f"{self.__age}")
a=person(21)
a.sub()

class ATM:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
    def deposit(self,pin,amount):
        if pin==self.__pin:
             self.__balance+=amount
             return self.__balance
        else:
            print("wrong PIN doesnt allow access")
    def withdraw(self,pin,amount):
        if pin==self.__pin:
            self.__balance-=amount
            return self.__balance
        else:
            print("wrong PIN doesnt allow access")

a=ATM(2004,50)
print(a.deposit(2005,20))
print(a.withdraw(2004,40))


# polymorphism
class car:
    def move(self):
        print(f"car goes on raod")
class boat:
    def move(self):
        print(f"boat sails in sea")
class plane:
    def move(self):
        print(f"plane flies in sky")
def fun(obj):
    obj.move() #duck typing
a=car()
b=boat()
c=plane()
fun(a)
fun(b)
fun(c)


class Calculator:
    def add(self,*n):
        sum=0
        for i in n:
            sum+=i
        return sum
a=Calculator()
print(a.add(2,3,1))

# method overriding
class car:
    def car1(self):
        print("nothing")
class bike:
    def car1(self):
        print('even nothing here')
a=car()
a.car1()
b=bike()
b.car1()

class Animal:
    def sound(self):
        print("sound")
class Cat:
    def cat(self):
        print("cat says meow")
class Dog:
    def dog(self):
        print("dogs bark")
a=Animal()
a.sound()
b=Cat()
b.cat()
c=Dog()
c.dog()



    