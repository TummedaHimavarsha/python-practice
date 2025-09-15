class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print("Animals speak")
class Dog(Animal):
    def sound(self):
        print(f"{self.name} Dog bark")
class Cat(Animal):
    def sound(self):
        print(f"{self.name} cat says meow")
a=Animal("animal")
a.sound()
b=Dog("Marshall")
b.sound()
c=Cat("mango")
c.sound()

class Calculator:
    def calculate(self,a,b):
        pass
class Add(Calculator):
    def calculate(self,a,b):
        return a+b
class Sub(Calculator):
    def calculate(self, a, b):
        return a-b
cal=Calculator()
cal1=Add()
print(cal1.calculate(10,20))
cal2=Sub()
print(cal2.calculate(20,30))

class Transport:
    def fare(self,distance):
        self.distance=distance
        print(f"the distnace from hyd to vizag is roughly {self.distance}kms")
class Bus(Transport):
    def fare(self,distance):
        f=distance*10
        return f
class Train(Transport):
    def fare(self,distance):
        f=distance*5
        return f
a=Transport()
print(a.fare(50))
b=Bus()
print(b.fare(50))
c=Train()
print(c.fare(50))

class Shape:
    def area(self):
        print("every shape has a area")
class Square(Shape):
    def area(self,side):
        return side*side
class Circle(Shape):
    def area(self,radius):
        return 3.14*radius*radius
a=Shape()
print(a.area())
b=Square()
print(b.area(2))
c=Circle()
print(c.area(1))
    
class Employee:
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print("writing code")
class Tester(Employee):
    def work(self):
        print("Testing software")
employees = [Developer(), Tester()]
for emp in employees:
    emp.work()


class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(2), Circle(1)]
for s in shapes:
    print(s.area())

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car started")
class Bike(Vehicle):
    def start(self):
        print("bike started")
a=Car()
a.start()
b=Bike()
b.start()
"""# vehicles=[Car(),Bike()]
# for i in vehicles:
#     print(i.start())"""

from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
class SavingsAccount(BankAccount):
    def withdraw(self):
        print('Withdrawn from savings')
class CurrentAccount(BankAccount):
    def withdraw(self):
        print('Withdrawn from current')
b=SavingsAccount()
b.withdraw()
c=CurrentAccount()
c.withdraw()

from abc import ABC,abstractmethod 
class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass
class TV(Device):
    def power_on(self):
        print("Tv is on")
class Laptop(Device):
    def power_on(self):
        print("Laptop is on")
a=TV()
a.power_on()
b=Laptop()
b.power_on()

from abc import ABC,abstractmethod
class Exam(ABC):
    @abstractmethod
    def start_exam(self):
        pass
class MathExam(Exam):
    def start_exam(self):
        print("math exam started")
class EnglishExam(Exam):
    def start_exam(self):
        print("English exam started")
a=MathExam()
a.start_exam()
b=EnglishExam()
b.start_exam()        

from abc import ABC,abstractmethod
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass
class PDFReport(Report):
    def generate(self):
        print("PDF Report generated")
class ExcelReport(Report):
    def generate(self):
        print("Excel Report generated")
a=PDFReport()
a.generate()
b=ExcelReport()
b.generate()





    


    



