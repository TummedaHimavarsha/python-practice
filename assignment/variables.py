salary=int(input("enter the salary: "))
hike=int(input("enter the increment: "))
increment=salary*hike/100
updated=salary+increment
print(updated)

celsius=int(input("enter the temperature: "))
fahrenheit=celsius+32*9/5
print(fahrenheit)

price=int(input("enter the price: "))
gst=int(input("enter the gst: "))
increment=price*gst/100
final_amount=price+increment
print(final_amount)

a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)

base=10
height=1
area=1/2*base*height
print(area)

num=int(input("enter a number: "))
if num&1==0:
    print("even")
else:
    print("odd")

num=10.12345
print(round(num,2))

num = 5.123
temp = num * 100
temp = temp + 0.5
rounded = int(temp) / 100
print(rounded)

price=int(input("enter ththe price: "))
discount=int(input("enter the discount: "))
discountamount=price*discount/100
sellingprice=price-discountamount
print(sellingprice)


principal=int(input("enter the principal: "))
rate=int(input("enter the rate: "))
time=int(input("enter the amount: "))
simple_interest=(principal*rate*time)/100
print(simple_interest)


a=100
b=100
a>b and print("a is larger")
a<b and print("b is larger")
a==b and print("both numbers are equal")

units=int(input("enter the units: "))
if units<100:
    print(units*5)
elif units==100:
    print(units*7)
else:
    print(units*10)


11,12


a=12345
digit=a%10
print(digit)

a=234
while a>10:
    a=a//10
print(a)

num=int(input("enter a number: "))
if num==0:
    print("equal to zero")
elif num>0:
    print("positive")
else:
    print("negative")

age=int(input("enter your birth year: "))
days=age*365
print(days)

costprice=int(input("enter the cost: "))
sellingprice=int(input("enter the selling price: "))
if sellingprice>costprice:
    profit=sellingprice-costprice
    print(profit,": is the profit amount")
else:
    loss=costprice-sellingprice
    print(loss,":is the loss amount")

a=input("enter a character: ")
ch=ord(a)
print(ch)

a="Tummeda"
b="Himavarsha"
print(a+b)

a="Himavarsha"
c=0
for i in a:
    c+=1
print(c)

a=complex(input("enter the complex number: "))
b=complex(input("enter the complex number: "))
print(a+b)

21

telugu=int(input("enter the marks scored: "))
hindi=int(input("enter the marks scored: "))
english=int(input("enter the marks scored: "))
maths=int(input("enter the marks scored: "))
science=int(input("enter the marks scored: "))
total=telugu+hindi+english+maths+science
percentage=total/5
print(total)
print(percentage)

days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
total_minutes = (days * 24 * 60) + (hours * 60)
print("Total minutes =", total_minutes)

year=int(input("enter the year: "))
if year%400==0 or year%4==0 and year%100!=0:
    print(f"{year}: is a leap year")
else:
    print(f"{year}: is not a leap year")

a=1000
b=200
c=30
if a>b and a>c:
    print(f"{a} is larger")
elif b>a and b>c:
    print(f"{b} is larger")
elif c>b and c>a:
    print(f"{c} is larger")

a="123"
b=int(a)
c=b+10
print(c)

a=10
b=102.0
c="hima"
d=[1,2,3]
e={"name":"porsche"}
f={1,2,3,"bmw"}
g=(1,2,3)
h=0+1j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

28

princinpal=int(input("enter: "))
rate=int(input("enter: "))
time=int(input("enter: "))
compound_interest=princinpal*(1+rate/100)**time
print(compound_interest)

s = input("Enter a string: ")
length = len(s)

if length % 2 == 0:
    mid1 = length // 2 - 1
    mid2 = length // 2
    print(s[mid1] + s[mid2])
else:
    mid = length // 2
    print(s[mid])

