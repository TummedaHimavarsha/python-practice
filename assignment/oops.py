# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
# car1=Car("porsche",911,1995)
# print(f"{car1.brand} has the highest model called {car1.model} in the year {car1.year}")
# car2=Car("bmw","m4",2000)
# print(f' the name of the car is:{car2.brand} and the version of it is {car2.model} in the year {car2.year}')
# car3=Car("Supra","ratata",1996)
# print(f"The {car3.brand} sounds {car3.model} in the year {car1.year}")
# car4=Car("koeingseg","A24",1994)
# print(f"my favorite car is {car4.model} anf the model is of the car is {car4.model} in the year {car1.year}")

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def engine(self):
#         print(f"{car1.brand} {car1.model} is started in the year {car1.year}")
#     def engine1(self):
#         print(f"{car2.brand} {car2.model} is started in the year {car2.year}")
#     def engine2(self):
#          print(f"{car3.brand} {car3.model} is started in the year {car3.year}")
#     def engine3(self):
#         print(f"{car4.brand} {car4.model} is stopped in the year {car4.year}")
# car1=Car("porsche",911,1995)
# car2=Car("bmw","m4",2000)
# car3=Car("Supra","ratata",1996)
# car4=Car("koeingseg","A24",1994)
# car1.engine()
# car1.engine1()
# car3.engine2()
# car4.engine3()



#class is the blueprint of an object,object is the instance of class

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def details(self):
#         print(f"{self.name} and age is {self.age}")
# s=student("prasannakshi",21)
# s.details()

# class define:
#     def __init__(self):
#         pass

"""self keyword is used inside a class to know which object is currently accessing the data and 
functions inside the class""" 


# class rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print(f"the area of the rectangle is:{self.length*self.width}")
# values=rectangle(2,3)
# values.area()

# f"the area of the rectangle is: {self.length}*{self.width}

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print(f"name of the employee is {self.name} and his salary is {self.salary}")
# employee_details=Employee("raghu",40000)
# employee_details.display()


# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print(f"the area of the circle is :{3.14*self.radius**2}")
# values=circle(2)
# values.area()

# class bankaccount:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance
#     def deposit(self):
#         print(f"The account number is{self.account_number} and the ramining balance is {self.balance}")
#     def withdraw(self):
#         print(f"The account number is{self.account_number} and the ramining balance is {self.balance}")
# v1=bankaccount(1234,24000)
# v2=bankaccount(4567,1000)
# v1.deposit()
# v2.withdraw()

# class bankaccount:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance
#     def deposit(self):
#         print(f"The account number is{self.account_number} and the ramining balance is {self.balance}")
# v1=bankaccount(1234,24000)
# v2=bankaccount(4567,1000)
# v1.deposit()
# v2.deposit()

class Book:
    def __init__(self,title, author,price):
        self.title=title
        self.price=price
        self.author=author
    def discount(self):
        print(f"the title of the book is {self.title} and the author of the book is {self.author} and the price of the book is {self.price}")
        print(f"the price of the book after the discount is {self.price*10/100-self.price}")
values=Book("starts with us","coollen hover",100)
values.discount()
        
        
    
    