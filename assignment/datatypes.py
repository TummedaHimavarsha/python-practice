a=10
b=20
temp=0
temp=a
a=b
b=temp
print(a,b)#swap two numbers
a,b=b,a
print(a,b)#swap using tuple unpacking

#input three values from the user and print their types
a=int(input("enter the number: "))
b=input("enter a string: ")
c=float(input("enter a number: "))
d=list(input("enter a list: "))
print(type(a),type(b),type(c),type(d))

simple calculator
a=int(input("enter a number: "))
b=int(input("enter a number: "))
print(f"addition of {a} and {b} are {a+b}")
print(f"subtraction of {a} and {b} are {a-b}")
print(f"multiplication of {a} and {b} are {a*b}")
print(f"modulus of of {a} and {b} are {a%b}")
print(f"division of {a} and {b} are {a/b}")
print(f"floor divion of {a} and {b} are {a//b}")
print(f"exponent of {a} and {b} are {a**b}")

#salary hike
salary=int(input("enter your salary: "))
a=115/100*salary
print(f"you will get 15% hike on ur salary then ur new salary will be: {a}")
print(f" your old salary is :{salary}")

ASCII


CHECK EVEN OR ODD
a=int(input("enter a number: "))
if a%2==0:
    print(f"the given number {a} is even ")
else:
    print(f" the given number {a} is odd")


compound assignment
a=int(input("enter a number: "))
b=int(input("enter a number: "))
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)
a//=b
print(a)
a**=b
print(a)


logical
age=int(input("enter your age: "))
name=input("enter your name: ")
if age==20 and name=="himavarsha" or age<=20:
    print("your not a robot")
else:
    print("u r a robot")


bitwise left and right
a=2
b=3
c=a<<b
d=a>>b
print(c)
print(d)

bitwise and or not xor
a=12
b=15
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)

datatype conversion
a=input("enter a string: ")
b=float(input("enetr a number: "))
c=int(input("enter a number: "))
x=int(a)
y=str(b)
z=bool(c)
print(x)
print(y)
print(z)
print(type(x),type(y),type(z))

a=10
b=20
print(a%b)
print(a//b)


string="hima Varsha"
print(string.upper())
print(string.lower())
print(len(string))
print("a" in string)
print("z" in string)


sum
a=1234
sum=0
while a>0:
    digit=a%10
    sum=sum+digit
    a=a//10
print(sum)

list=[11,2,3]
list1=[2,4,5]
print(list is list1)
print(list is not list1)
print(list==list1)

x=10+3.5
print(type(x))
y="age: "+str(30)
print(y)
z=True+False+2
print(z)

n=10
print(~n)
print(n<<1)
print(n>>1)
