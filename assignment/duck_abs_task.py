# class Duck:
#     def walk(self):
#         print("duck can walk")
# class Person:
#     def walk(self):
#         print("humans can walk")
# def make_it_walk(obj):
#     obj.walk()
# a=Duck()
# make_it_walk(a)
# b=Person()
# make_it_walk(b)

# class Mp3:
#     def play(self):
#         print("mp3 plays songs")
# class Video:
#     def play(self):
#         print("video plays the videos")
# def start_media(obj):
#     obj.play()
# a=Mp3()
# start_media(a)
# videos=Video()
# start_media(videos)

# class Creditcard:
#     def __init__(self,amount):
#         self.amount=amount
#     def pay(self,amount):
#         print(f"Paid {amount} using Credit Card. Available balance: {self.amount}")
# class UPI:
#     def pay(self,amount):
#         print(f"Paid {amount} using UPI.")
# def process_payment(obj,amount):
#     obj.pay(amount)
# a=Creditcard(200)
# process_payment(a,100)
# b=UPI()
# process_payment(b,50)

# #ABSTRACTION
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Square:
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side*self.side
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius*self.radius
# a=Square(5)
# print(a.area())
# b=Circle(1)
# print(b.area())

# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Car:
#     def start(self):
#         print("Car is started")
# class Bike:
#     def start(self):
#         print("Bike is started")
# a=Car()
# a.start()
# b=Bike()
# b.start()


# from abc import ABC,abstractmethod
# class BankAccount(ABC):
#     @abstractmethod
#     def withdraw(self,amount):
#         pass
# class Savings:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if self.balance - amount >= 500:  # must maintain min balance 500
#             self.balance -= amount
#             return f"Withdrawal successful. Remaining balance: {self.balance}"
#         else:
#             return "Insufficient balance to maintain minimum required balance."
# class Current:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#             if amount <= self.balance:
#                 self.balance -= amount
#                 return f"Withdrawal successful. Remaining balance: {self.balance}"
#             else:
#                 return "Insufficient funds!"
# a=Savings(1000)
# print(a.withdraw(200))
# print(a.withdraw(600))
# b=Current(200)
# print(b.withdraw(100))
# print(b.withdraw(200))   
# from abc import ABC,abstractmethod
# class Report(ABC):
#     @abstractmethod
#     def generate(self):
#         pass
# class PDFReport(Report):
#     def generate(self):
#         print("PDF Report generated")
# class ExcelReport(Report):
#     def generate(self):
#         print("Excel Report generated")
# a=PDFReport()
# a.generate()
# b=ExcelReport()
# b.generate()

# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def work(self):
#         pass
# class Developer():
#     def work(self):
#         print("writing code")
# class Tester(Employee):
#     def work(self):
#         print("Testing software")
# a=Developer()
# a.work()
# b=Tester()
# b.work()

from abc import ABC,abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class Fan:
    def turn_on(self):
        print("Fan is turned on")
class Light:
    def turn_on(self):
        print("Light is turned on")
a=Fan()
a.turn_on()
b=Light()
b.turn_on()



