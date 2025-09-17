class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}, New Balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: {amount}, New Balance: {self.balance}"
        else:
            return "Insufficient balance"
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        BankAccount.__init__(self, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return f"Interest Added: {interest}, New Balance: {self.balance}"
b = BankAccount(2001, 1000)
print(b.deposit(500))       
print(b.withdraw(300))      
s = SavingsAccount(3001, 2000, 5)
print(s.add_interest()) 

class library:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def Book(self,title,author):
        print(f"The title of the book is {self.title} and the author of the book is {self.author}")
class Ebook(library):
    def __init__(self,file_size,title,author):
        self.file_size=file_size
        self.title=title
        self.author=author
    def download(self,file_size,title):
        print(f"The size of the book for {self.title} is {self.file_size} ")
a=Ebook("25kb","harrypotter","J.K.Rowling")
a.Book("harry potter","J.K.Rowling")
a.download("25kb","harrypotter")

class management:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def Employee(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
class management1(management):
    def __init__(self,name,salary,programming_language):
        management.__init__(self,name,salary)
        self.programming_language=programming_language
    def skills(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary} and she know {self.programming_language}")
a=management1("himavarsha",100000,"python full stack")
a.Employee()
a.skills()

class Camera :
    def take_photo(self):
        print("The camers is used to take photos and videos")
class Musicplayer:
    def play_music(self):
        print("Music player is used to play amazing music tracks")
class smartphone(Camera,Musicplayer):
    def info(self):
        print("The smart phone has both camera as well as music player as a builtin")
a=smartphone()
a.take_photo()
a.play_music()
a.info()

class Engine:
    def start_engine(self):
        print("The engine will be started when the keys is inserted")
class Wheels:
    def rotate_wheels(self):
        print("when the steering is roataed automatically the wheels also rotate")
class Car(Engine,Wheels):
    def info(self):
        print("The engine and wheels are the feature and parts of the car")
a=Car()
a.info()
a.start_engine()
a.rotate_wheels()

class Doctor:
    def treat_patient(self):
        print("Doctor identifies the patient problem")
class Researcher:
    def conduct_research(self):
        print("Researcher identifies in depth")
class Doctorresearch(Doctor,Researcher):
    pass
a=Doctorresearch()
a.treat_patient()
a.conduct_research()

class Person:
    def __init__(self,name):
        self.name=name
    def details(self):
        print(f"The name of the person is {self.name}")
class Teacher(Person):
    def __init__(self,name,subject):
        Person.__init__(self,name)
        self.subject=subject
    def details1(self):
        print(f"The name of the person is {self.name} and fav subject is {self.subject}")
class HOD(Teacher):
    def __init__(self,name,subject,deptname):
        Teacher.__init__(self,name,subject)
        self.deptname=deptname
    def details2(self):
        print(f"The hod of {self.deptname} department is very strict")
a=HOD("John","Data structures","CSE")
a.details()
a.details1()
a.details2()

class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def info(self):
        print(f"The name of the product is {self.name} and it costs {self.price}")
class Electronics(product):
     def __init__(self,name,price,brand):
        product.__init__(self,name,price)
        self.brand=brand
     def info1(self):
        print(f"The brand name of the {self.name} is {self.brand}")
class Mobile(Electronics):
    def __init__(self,name,price,brand,ram,storage):
        Electronics.__init__(self,name,price,brand)
        self.ram=ram
        self.storage=storage
    def info2(self):
        print(f"The ram of the mobile is {self.ram} and the storage is {self.storage}")
a=Mobile("device",75000,"samsung","12Gb","320")
a.info()
a.info1()
a.info2()

class Vehicle:
    def __init__(self,speed):
        self.speed=speed
    def info(self):
        print(f"The car highest speed is {self.speed}")
class Car(Vehicle):
    def __init__(self,speed,fuel_type):
        Vehicle.__init__(self,speed)
        self.fuel_type=fuel_type
    def info1(self):
        print(f"The fuel type of the vehicle is {self.fuel_type}")
class Electriccar(Car):
    def __init__(self,speed,fuel_type,battery_capacity):
        Car.__init__(self,speed,fuel_type)
        self.battery_capacity=battery_capacity
    def info2(self):
        print(f"The battery capacity of the elecric vehicle is {self.battery_capacity}")
a=Electriccar("360km/h","petrol","85")
a.info()
a.info1()
a.info2()