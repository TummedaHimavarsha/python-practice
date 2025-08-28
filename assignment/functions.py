def cube(a):
    b=a**3
    return b
print(cube(2))

def avg(a,b):
    return (a+b)/2
print(avg(10,20))

def sqr(a):
    b=a*a
    c=a**0.5
    return b,c
print(sqr(16))

def is_odd(n):
    if n%2!=0:
        return "True"
    else:
        return "False"
print(is_odd(21))
    

def fun(n):
    sum=0
    for i in str(n):
        sum=sum+int(i)
    return sum
print(fun(12345))



def greet(name="Guest"):
    print(f"Hello! {name} ")
greet()


def power(base,exponent=2):
    return base**exponent
print(power(3))

def total_bill(item='Sandwich',quantity=1,price=50):
    if item=='Sandwich' and quantity==1:
        print(price)
    elif quantity>1:
        return quantity*price
print(total_bill(item='Sandwich',quantity=3))

def employee_info(name,age=30,department='HR'):
    print(f'my name is {name} and my age is {age} and i am {department} of mnc comapny')
employee_info(name="hima")

def circle_area(radius=1):
    area=3.14*radius*radius
    return area
print(circle_area())

def fun():
    n=int(input("enter a number: "))
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum=sum+i
    return(sum)
print(fun())


def num(n):
        return max(n)
print(num([1,2,3,24,5]))
        

def fun(num):
    a=num[0]
    for i in num:
        if i>a:
            a=i
    return a
print(fun([1,54,2,6]))


def min_max(numbers):
    return min(numbers),max(numbers)
print(min_max([12,4,6,78,94563,23]))

def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest
print(min_max([12, 4, 6, 78, 94563, 23]))



def student_summary(name, marks):
    total = sum(marks)              
    avg = total / len(marks)        
    return name, total, avg
print(student_summary("Hima", [80, 90, 85, 95]))



def fun(num1,num2,operator='+'):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"
print(fun(2,4,"-"))
