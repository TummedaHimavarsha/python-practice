"""def display_message():
    a='msg'
display_message()
print(a) """ # This will raise a NameError since 'a' is not defined in the global scope.
"""def add_numbers():
    a=10
    b=20
    c=a+b
    print(c)
add_numbers() 
print(c)""" # This will print 30, as 'a' and 'b' are defined within the function scope.
"""counter=0
def increase_counter():
    counter=counter+1
    print(counter)
# This will raise an UnboundLocalError since 'counter' is referenced before assignment
increase_counter()"""
"""counter = 0
def increase_counter():
    global counter
    counter += 1
    print(counter)
increase_counter()"""  # This will print 1, as 'counter' is now defined in the global scope.
"""students = ['Alice', 'Bob', 'Charlie']
def add_student(name):
    students.append(name)
add_student("marshall")
print(students)"""  # This will print ['Alice', 'Bob', 'Charlie', 'marshall'], as 'students' is modified in the global scope.
"""def fun():
    language='python'
    def fun1():
        print(language)
    fun1()
fun()"""
"""def fun():
    language='python'
    def fun1():
        nonlocal language
        language='java'
        print(language)
    fun1()
fun()"""
"""def outer():
    value=10
    def inner():
        nonlocal value
        value=20
        print(value)
    inner()
outer()"""
"""name="Alice"
def func():
    print(name)
    name="Bob"
    print(name)
func()
print(name)"""
# 2 i dont know
def bank_account():
    balance=1000
    def deposit(amount):
        def withdraw(amount):
            nonlocal balance
            balance=2000
            print(balance)
        withdraw(2)
        print(balance)
    deposit(3)
bank_account()
