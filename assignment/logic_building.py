celsius=int(input("enter: "))
f=(celsius*9/5+32)
print(f)

def temp():
    celsius=int(input("enter"))
    f=(celsius*9/5+32)
    return f
print(temp())

calculate net salary after adding allowances and removing deductions

def net():
    basicsalary=int(input("enter the basic salary: "))
    allowances=int(input("enter the allowances: "))
    deductions=int(input("enter the deductions: "))
    netsalary=basicsalary+allowances-deductions
    return netsalary
print(net())

def net( basicsalary,allowances,deductions):
    netsalary=basicsalary+allowances-deductions
    return netsalary
print(net(10,20,10))

find the area of a circle
def circle():
    radius=int(input("enter the radius: "))
    area=3.14*radius**2
    return area
print(circle())

calculate simple interest for an amount
simple_interest=(principal*rate_of_interest*time)/100
def pay():
    principal=int(input("enter principal amount: "))
    rate_of_interest=int(input("enter rate of interest: "))
    time=int(input("enter the time: "))
    simple_interest=(principal*rate_of_interest*time)/100
    return simple_interest
print(pay())

calculate average of marks of a student for 3 subjects  
avg=sum of acquired marks/sum of max marks  
def marks():

    telugu=int(input("enter the marks: "))
    hindi=int(input("enter the marks: "))
    maths=int(input("enter the marks: "))
    avg=telugu/telugu+hindi+maths
    return avg
print(marks())

def swap():
    a,b=10,20
    a,b=b,a
    return a,b
print(swap())
 

def swap(a,b,c):
    c=a
    a=b
    b=c
    return a,b
print(swap(10,20,0))

calculate percentage of amount spent on groceries,bills, and transport from  a salary
def calculate(salary,groceries,bills,transport):
    total_expenses=((groceries+bills+transport)/salary)*100
    return total_expenses
print(calculate(25000,5000,5000,2000))

calculate speed of  a bike 
def porsche(distance,time):
    hour=time/60
    speed=distance*hour
    return speed
print(porsche(200,10))


calculate age of a person: age=current year-year of birth 
calculate km into m and cm convert hours into minutes and seconds 