hierarchical inheritance
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def info(self):
        print(f"The name of the employee is {self.name} and the id is {self.id}")
class child(Employee):
    def __init__(self,name,id,programming_language):
        Employee.__init__(self,name,id)
        self.programming_language=programming_language
    def info1(self):
        print(f"The most known programming language is {self.programming_language}")
class Manager(Employee):
     def __init__(self,name,id,programming_language,team_size):
        child.__init__(self,name,id,programming_language)
        self.team_size=team_size
     def info2(self):
        print(f"The manager team size consists of {self.team_size} members")
b=Employee("moksha",2345)
b.info()
c=child("moksha",2345,"python")
c.info1()
d=Manager("moksha",2345,"python","5")
d.info2()

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"{3.14*self.radius*self.radius}")
b=Rectangle(2,3)
print(b.area())
c=Circle(5)
c.area()

class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def info(self):
        print(f"The brand of the car is {self.brand}, and it was intoduced in the year {self.year}")
class Car(Vehicle):
    def __init__(self,brand,year,doors):
        Vehicle.__init__(self,brand,year)
        self.doors=doors
    def info1(self):
        print(f"The doors are made of {self.doors}")
class Bike(Vehicle):
     def __init__(self,brand,year,doors,type):
        Car.__init__(self,brand,year,doors)
        self.type=type
     def info2(self):
        print(f"The bike is of {self.type} type")
a=Car("bmw",1995,"metal")
a.info1()
b=Bike("interceptor",1990,"metal","petrol")
b.info2()
c=Vehicle("minicooper","2005")
c.info()

hybrid inheritance

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"The name of the person is {self.name} and the age is {self.age}")
class Student(Person):
    pass
class Sports(Person):
    def __init__(self,name,age,sportsactivity):
     super().__init__(name,age)
     self.sportsactivity=sportsactivity
    def info(self):
        super().info()
        print(f"{self.sportsactivity}")
class CollegeStudents(Student,Sports):
    def info1(self):
        print(f"{self.name},{self.age},{self.sportsactivity}")
a=CollegeStudents("PV sindhu",30,"badminton")
a.info1()
b=Person("PV sindhu",30)
b.info()
c=Sports("PV sindhu",30,"badminton")

class staff:
    def info0(self):
        print("2000+ staff members working in this school")
class Teacher(staff):
    def info1(self):
        print("The telugu teacher is 5 years experienced candidate")
class Researcher(staff):
    def info2(self):
        print("The researcher is very much useful in laboratories")
class professor(Teacher,Researcher):
    def info3(self):
        print("professor teaches in colleges")
        print(professor.__mro__)
a=professor()
a.info2()
a.info1()
a.info3()
b=Researcher()
b.info0()
b.info2()

class Product:
    def info1(self):
        print("Bajaj show room consist of so many electronic gadgets")
class Electronics(Product):
    def info2(self):
        print("Vijay sales has strong and so many varieties of gadgets")
class Accessories(Product):
    def info3(self):
        print("pie is the best for electonics like home appliances")
class Smartphones(Electronics,Accessories):
    pass
a=Smartphones()
a.info3()
a.info2()
b=Electronics()
b.info1()

super
class Fee:
    def Calculate(self):
       print("The school fee is 20k")
class Tutionfee(Fee):
    def Calculate(self):
        super().Calculate()
        print("Tution fee")
a=Tutionfee()
a.Calculate()

class Account:
    def deposit(self):
        print("5000 rupees")
class savings(Account):
    def deposit(self):
        super().deposit()
        print("saves 100 rupees")
a=savings()
a.deposit()

class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        super().show()
        print("B")
class C(B):
    def show(self):
        super().show()
        print("C")
        print(C.__mro__)
a=C()
a.show()

mro method resolution order task
class A:
    def display(self):
        print("asus")
class B(A):
    def display(self):
        super().display()
        print("Dell")
class C(A):
    def display(self):
        super().display()
        print("Lenovo")
class D(B,C):
    pass

a=D()
a.display()
print(D.__mro__)


class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
a=D()
print(D.__mro__)

class Book:
    def info(self):
        pass
class EBook(Book):
    def info(self):
        super().info()
        print("Ebook")
class AudioBook(Book):
    def info(self):
        super().info()
        print("Audiobook")
class  DigitalLibrary(EBook, AudioBook):
    pass
a=DigitalLibrary()
a.info()
print( DigitalLibrary.mro())