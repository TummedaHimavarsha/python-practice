n=input("enter a string: ")
rev = 0
while n > 0:
    digit = n % 10        # last digit
    rev = rev * 10 + digit
    n = n // 10           # remove last digit
print(rev)


list=[1,8,3,1]
print(max(list))
sum=0
for i in list:
    sum=sum+i
print(sum)

for i in range(1,4):
    username=input("enter your username: ")
    password=input("enter your password: ")
    if username=="admin" and password=="Admin@123":
        print("Log in Successful!!!")
        break
else:
    print("account is locked")


selected_seats=int(input("enter the seat number:"))
if selected_seats%3==0 and selected_seats%5==0:
     print("your eligible for the discount of 100 rupees")
else:
    print(" sorry your not eligible for the discount")


items=["apples", "banana", "capsicums", "bread", "onions"]
neededItem=input("Enter the item you are looking for: ")
for i in items:
    if i==neededItem:
        print("available")
        break
else:
    print("not available")
list=[1,2,3,4,5,6,7]
odd_count=0
evn=0
for i in list:
    if i%2==0:
        evn=evn+1
    else:
        odd_count=odd_count+1
print(f"even numbers in the list are :{evn}")
print(f"odd numbers in the list are :{odd_count}")
marks=[400,450,530,550,570,2]
avg=0
for i in marks:
    avg=avg+i
print(avg/2)
a=b=c=5
if a+b>c and a+c>b and b+c>a:
    print("it forms a triangle")
else:
    print("it does not form a triangle")

s=input("enter a string: ")
rev=" "
for i in s:
    rev=i+rev
print(rev)


a=10
b=20
# a,b=b,a
# print(a,b)
temp=0
temp=a
a=b
b=temp
print(a,b)  

radius=int(input("enter the radius of the circle: "))
area=3.14*radius*radius
circumference=2*3.14*radius
print(area,circumference)

c=int(input("enter the temperature in celsius: "))
f=int(input("enter the temperature in fahrenheit: "))
f=9/5*c+32
c=(f-32)*5/9
print(f,c)
a=int(input("enter a number: "))
if a%2==0:
    print("even")
else:
    print("odd")
a=int(input("enter a number: "))
b=a*a
print(f'The square of the given number is:{b}')

print(5 and 0)
print(0 or 7)
print(not 10 > 5)

a=int(input("enter a number: "))
if a%4== 0 and a%100 != 0 or a%400 == 0:
    print("leap year")
else:
    print("not a leap year")
pin=int(input("enter the pin: "))
balance=24000000
if pin==2004:
    print(f'ur total remaining balance in ur account is :{balance}')
else:
    print("invalid pin")
for i in range(1,21):
    if i%3==0:
        continue
    print(i)
for i in range(1,50):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                print('not a prime number')
                break
        else:
            print("prime number")
else:
    print("not a prime number")
def fun():
    pass
fun()
a=int(input("enter a number:"))
for i in range(1,11):
    b=a*i
    print(b)
a=123
rem=0
while a>0:
    digit=a%10
    rem=rem*10+digit
    a=a//10
print(rem)
a=int(input("enter a number:"))
fact=1
while a>0:
    fact=fact*a
    a=a-1
print(fact)
for i in range(5):
    print(i, end=" ")
num=int(input("enter a number: "))
def fun():
    fact=1
    for i in range(1,num):
        fact=fact*i
        print(fact)
fun()
s="himavarsha"
rev=" "
for i in s:
    rev=i+rev
print(rev)

n=10
a,b=0,1
for i in  range(n):
    print(a,end=' ')
    a,b=b,a+b
def fun():
    list=[1,2,3,4,5]
    n=max(list)
    b=min(list)
    c=sum(list)/len(list)
    print(n)
    print(b)
    print(c)
fun()
def f(name="hima",age=21,msg="welcome!"):
    print(f"{msg} my name is {name},my age is {age}")
f("jyo")
def power(base,exp):
    pwr=base**exp
    print(pwr)
power(2,5)
def student(name,age,course):
    print(f"my name is {name} and my age is {age} and i from the {course}")
student(age=20,course="python",name="varshini")
def func(*n):
    sum=0
    for i in n:
        sum=sum+i
    print(sum)
func(1,2,3,5)
def fun(**n):
    for i,j in n.items():
        print(i,j)
fun(name='hima',age=20,course='python')
# a=10
# def fun():
#     global a
#     a=a+10
#     print(a)
# fun()
# print(a)
def fun():
    a=10
    print(a)
fun()
def fun():
    a=10
    def defaults():
        nonlocal a
        a=a+10
        print(a)
    defaults()
fun()
a="aeiou"
count=0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count=count+1
print(count)
a="121"
if a==a[::-1]:
    print(f"{a} is palindrome")
else:
    print(f"{a} is not a palindrome")
# s="    hima    "
# print(s.strip())

s="python programming"
print(s.title())
password=input("enter a string: ")
if password=="Hima@2004":
    print("accepted")
else:
    print("not accpeted")
list1=[1,2,3,4,5]
a=min(list1)
b=max(list1)
c=sum(list1)/len(list1)
print(a)
print(b)
print(c)

nums = [1, 2, 3]
nums.append([4, 5])
print(nums)

tu=(1,2,3)
print(tu.index(4))
lis=[1,2,3,4]
a=tuple(lis)
print(a)
tup=(1,2,3)
a=list(tup)
print(a)
set={1,2,3}
set1={1,2,3,4,3}
print(set.union(set1))
print(set.intersection(set1))

d = {"a":1, "b":2}
print(d.get("c", 0))
def example(val):
    val+=1
    return val
print(example(6))

for i in range(5):
    if i==3:
        break
    print(i,end=" ")
else:
    print("done")
for i in range(5):
    if i==2:
        continue
    if i==4:
        break
    print(i)
x=0
for i in range(10):
    if i %2==0:
        continue
    if i>5:
        break 
    x+=i
print(x)
for i in range(10):
    if i==5:
        break
    if i%2==0:
        continue
    print("hello")