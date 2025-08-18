# Task 1: Greeting a user
"""a="Himavarsha"
print(f"Hello {a}, good morning!")"""
#Store two numbers in variables and print their sum
"""a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
sum=a+b
print(f'addition of {a} and {b} is {sum}')"""
# Store the price of an item and quantity, then print the total cost
"""price=int(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity of the item: "))
total_cost=price*quantity
print(f"The total cost is {total_cost}")"""
#Store your age in a variable and print how many years are left until you turn 100
"""age=int(input("enter your age:"))
left_over_age=100-age
print(f'The left over age you to survive is {left_over_age}')"""
#Swap the values of two variables without using a third variable.
"""a=int(input("enterr a number: "))
b=int(input("enterr a number: "))
a,b=b,a
print(a)
print(b)"""
#2. Data Types
#Create a list of three fruits and print the second one
"""list=["apple","mosambi","dragon"]
print(list[1])"""
#Store a sentence in a string and print its length.
"""a="Hi Himavarsha the founder of a big MNC Ccomapny in future"
print(len(a))"""
# Create a tuple of five integers and print the maximum number
"""a=(1,2,3,44,5)
max=0
for i in a:
    max=i
print(max)"""
#Create a dictionary with three student names as keys and their marks as values, then print the marks of
 #one student.
"""a={"Himavarsha":49,"Jyothika":48,"Prasannakshi":48}
print(a["Prasannakshi"])"""
#Convert a string '123' into an integer and print its double.
"""string='123'
integer=int(string)
print(integer*integer)
"""
#4. Conditional Statements
 #1. Take a number and print 'Positive' if greater than zero, else 'Negative'
"""a=int(input("enter a number: "))
if a>0:
    print("positive")
else:
    print("Negative")
"""
#2. Take an age and print if the person is a child, teenager, or adult.
"""age=int(input("enter your age: "))
if age<=12:
    print("Child")
elif age<=19:
    print("teenager")
else:
    print("adult")
"""
 #3. Take three numbers and print the largest one.
"""a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
if a>b and a>c:
    print(f'{a} is the largest number than {b} and {c}')
elif b>a and b>c:
    print(f'{b} is the largest number than {a} and {c}')
else:
    print(f'{c} is the largest number than {a} and {b}')"""
#5. Take a mark and print 'Pass' if it is 40 or more, otherwise 'Fail'
"""marks=int(input("enter a number: "))
if marks>=40:
    print("Pass")
else:
    print("Fail")"""
# 5. Control Statements
#1. Print numbers from 1 to 10, but skip the number 5 using continue
"""for i in range(1,11):
    if i==5:
        continue
    print(i)"""
#2. Print numbers from 1 to 20, but stop when you reach 13 using break.
"""for i in range(1,21):
    if i==13:
        break
    print(i)"""
# 3. Print all even numbers from 1 to 10, skipping odd numbers.
"""for i in range(1,11):
    if i%2!=0:
        continue
    print(i)"""
# 4. Use a loop to print numbers from 1 to 5, but use pass inside the loop body.
"""for i in range(1,6):
    pass
    print(i)"""
#5. Continuously take input from the user until they type 'exit'.
"""while True:
    a=input("enter a string: ")
    if a=="exit":
        break"""
# 6. Loops
 #1. Print numbers from 1 to 10 using a for loop
"""for i in range(1,11):
    print(i)"""
#2. Print numbers from 10 to 1 using a while loop.
"""i=10
while i>=1:
    print(i)
    i-=1
"""
#. Print the sum of numbers from 1 to 100
"""sum=0
for i in range(1,101):
    sum=sum+i
    print(sum)"""
#4. Print all elements of a list using a loop
"""list=[1,"hima",2,"jyo"]
for i in list:
    print(i)"""
#. Take a number n and print its multiplication table from 1 to 10.
"""n=5
for i in range(1,11):
    a=n*i
    print(a)
"""
#7. User-Defined Functions
#1. Write a function that takes a name and prints 'Hello, <name>!'
"""def function():
    name=input("enter a name: ")
    print(f"Hello {name}")
function()"""
# 2. Write a function that takes two numbers and returns their sum.
"""def sum():
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    sum=a+b
    return sum
print(sum())"""
# 3. Write a function that checks if a number is even or odd
"""def even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
even_odd(20)"""
# Write a function that takes a list of numbers and returns the largest one
"""# 5. Write a function that takes a number and returns its factorial.
def fact():
    n=int(input("enter a number: "))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(fact())"""
#operators
# 1. Take two numbers and print their sum, difference, product, and quotient.
"""a=int(input("enter a number: "))
b=int(input("enter a number: "))
print(a + b,a-b,a*b,a/b)"""
# 2. Take a number and check if it's even or odd using % operator.
"""a=int(input("enter a number: "))
    if a%2==0:
        print("even")
    else:
        print("odd")"""

# 3. Check if 'apple' is in the list ['banana', 'apple', 'mango'].
"""list=["apple","banana","cherry"]
print("apple" in list)"""
#. Find the remainder when 29 is divided by 5.
"""n=29%5
print(n)"""
# 4. Take a number and check if it's between 10 and 50 (inclusive).
"""a=int(input("enter a number: "))
if a>=10 and a<=50:
    print(f"{a} is between 10 and 50")
else:
    print(f"{a} is not between 10 and 50")"""

