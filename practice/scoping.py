"""def local():
    x=5
print(x)  
local()"""# this will give error becoz it is outside the function
"""def local():
    x = 5# local variable
    print(x)
local() """ # This will print 5, as x is defined within the function scope
"""a=10
def globals():
    print(a)
globals()
print(a) # u can access the variable outside the function also
"""
"""def non_local():
    a=10
    def non1():
        print(a)# can be accessed in nested function that is inner function but not outside the fucntion
    non1()
non_local()# cannot access the varibale outside the function like print(a)"""
#built  in
"""max=5
print(max)"""
"""print=5
print(print)"""
"""x=10
def fun():
    x=5
    x+=5
    print(x)
fun()
print(x)"""# error

"""x=10
def fun():
    global x # global key word for to the new updated value outside the fuinction also
    x+=5
    print(x)
fun()
print(x)"""

"""def func():
    x=10
    def func1():
        nonlocal x  # nonlocal keyword to access the variable from the enclosing scope
        x+=5
        print(x)
    func1()
func()"""
"""x=10
def func():
  # using global keyword to modify the global variable
    x+=5
    print(x)
func()
print(x)"""  # this will print the updated value of x
