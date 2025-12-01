age=int(input("enter your age: "))
if age>18:
    print("eligible to vote")
else:
    print("you are not eligible to vote")

a=123
if len(str(a))==3:
    print("3 digit number")
else:
    print("not a 3 digit number")

marks=int(input("enter the marks secured: "))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Fail")

speed=int(input("enter the speed: "))
if speed>60:
    print("Fine")
else:
    print("Safe")


char="z"
if char in "aeiou":
    print("vowel")
else:
    print("constant")

balance=200
amount=int(input("enter the amount you want to with drawal: " ))
if balance>=200:
    amount=amount*100
    print(amount)
else:
    print("sorry there is no sufficient balance")


age=int(input("enter your number: "))
if age<=12:
    print("The ticket price is 50")
elif 13<=age<=19:
    print("The price of the ticket is 150")
else:
    print("The price of the ticket is 350")


a=102334567
b=20
c=10023
if a>b and a>c:
    print(a,"is larger")
elif b>a and b>c:
    print(b,"is larger")
else:
    print(c,"is larger")

year=int(input("enter the year: "))
if year%400==0 or (year%4==0 and year%100!=0):
    print(year,"IS A LEAP YEAR")
else:
    print(year,"is not a leap year")

num=int(input("enter a number: "))
b=num**0.5
if b==int(b):
    print("perfect square")
else:
    print("not a perfect square")

totalcost=int(input("enter the total bill cost: "))
if totalcost>500:
    discount=totalcost*2/100
    total=totalcost-discount
    print(total)
else:
    print("no discount,to avail this offer shop for 500 at max")


a=10
b=20
c=10
if (a+b)>c:
    print("Triangle is valid")
else:
    print("not a triangle")

years=int(input("enter the number of years: "))
salary=int(input("enter your salary: "))
if years>5:
    bonus=salary+5000
    print(bonus)
elif years==2:
    bonus=salary+2000
    print(bonus)
elif years==1:
    print("sorry a s you are a fresher there is no bonus for now")
else:
    bonus=salary+7000
    print(bonus)

celsius=int(input("enter temperature: "))
fahrenheit=(celsius*9/5)+32
if 32 <= fahrenheit < 50:
    print("Weather is: Cold / Autumn")
elif 50 <= fahrenheit < 70:
    print("Weather is: Cloudy")
elif 70 <= fahrenheit < 90:
    print("Weather is: Hot")
elif fahrenheit >= 90:
    print(" Weather is: Very Hot / Summer")
else:
    print("Weather is: Freezing / Snowy")


while loops:
n=2
i=1
while i<=10:
    print(f"{n}*{i}={n*i}")
    i+=1

a=123
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
print(rev)

num=1235
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)

a = int(input("Enter a number: "))
even = 0
odd = 0
while a > 0:
    digit = a % 10
    if digit % 2 == 0:
        even += 1
        print(digit, "even")
    else:
        odd += 1
        print(digit, "odd")
    a = a // 10
print("Even count:", even)
print("Odd count:", odd)


while True:
    user=int(input("enter the number: "))
    if user==0:
        break

n=3
fact=1
while n>0:
    fact=fact*n
    n-=1
print(fact)

n=int(input("Enter a number:"))
if n<=1:
    print("Not Prime")
else:
    i=2
    flag=1
    while i<=n//2:
        if n%i==0:
            flag=0
            break
        i+=1
    if flag==1:
        print("Prime")
    else:
        print("Not Prime")

while True:
    password=input("enter the password: ")
    if password=="admin":
        print("login successful")
        break

n=int(input("Enter number of terms:"))
a=0
b=1
i=1
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1


a="Himavarsha"
c=0
for i in a:
    if i in "aeiou":
        c+=1
print(c)


list1=[1111,22,333]
max=list1[0]
for i in list1:
    if i>max:
        max=i
print(max)

list1=[11,22,-3,0,8,222]
pos=0
neg=0
zero=0
for i in list1:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zero+=1
print("Positive:",pos)
print("Negative:",neg)
print("Zero:",zero)


num=6
for i in range(1,num+1):
    if num%i==0:
        print(i)

for i in range(1,101):
    if i%7==0:
        print(i)

a="himavarsha"
b=""
for i in a:
    if a.count(i)==1:
        b=b+i
print(b[0])

str="himavarsha"
for i in str:
    print(ord(i))


list1=[1,2,3,4,5]
sums=0
for i in list1:
    sums+=i
avg=sums/len(list1)
print(avg)


sums=0
for i in range(1,101):
    if i%2==0:
        sums+=i
print(sums)

for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="")
    print()

# nested if/loops

card=input("enter the type: ")
if card=="debit":
    amount=int(input("enter the amount that u want to with draw :"))
    pin=int(input("enter your pin: "))
    if pin==1234:
        print("success")
    else:
        print("wrong password⚠️")
else:
    print("not available only debit card is available")

username=input("enter the username: ")
if username=="admin123":
    password=input("enter your password: ")
    if password=="admin":
        print("login success")
    else:
        print("wrong password")
else:
    print("reenter")

str="admin@123"
for i in str:
    if i in "aeiou":
        print(i,"is a vowel")
    elif i in "abcdefghijklmnopqrstuvwxyz":
        print(i,"is a constant")
    elif i in"1234567890":
        if int(i)%2==0:
            print(i,"is a evennumber")
        else:
            print(i,"is a odd number")
    else:
        print(i,"special character")

for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()


password = input("Enter password: ")
upper = lower = digit = special = 0
special_chars = "!@#$%^&*()_+-=<>?/.,"
for ch in password:
    if 'A' <= ch <= 'Z':
        upper = 1
    elif 'a' <= ch <= 'z':
        lower = 1
    elif '0' <= ch <= '9':
        digit = 1
    elif ch in special_chars:
        special = 1
if upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")

dept=input("enter the dept name: ")
if dept=="icu":
    days=int(input("enter the number of days: "))
    total=1000*days
elif dept=="room":
    days=int(input("enter the number of days: "))
    total=500*days
else:
    print("no dept")
print(total)


category=input("enter the type: ")
if category=="maincourse" or category=="chinese" or category=="beverages":
    items=int(input("enter the no of items: "))
    total=items*500
else:
    print("not available")
print(total)

rows=int(input("enter which row u want to book: "))
columns=int(input("enter which column u want to book: "))
if rows==3 and columns==5:
    print("availabale")
else:
    print("not available")

a="himavarsha"
b=""
for i in a:
    if a.count(i)>1:
        print(i)

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print()

# control statements

while True:
    user=int(input("enter a number: "))
    if user<0:
        break

for i in range(1,11):
    if i%2!=0:
        continue
    else:
       print(i)

count = 0
num = 2

while count < 5:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    num += 1

def fun():
    for i in range(1,5):
        pass
fun()

str="ad32min123"
for i in str:
    if i.isdigit():
        continue
    else:
        print(i)
