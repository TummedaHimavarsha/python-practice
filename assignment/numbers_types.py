a=int(input("enter a number: "))
b=a*a
sum=0
for i in str(b):
    sum=sum+int(i)
if a==sum:
    print(sum,"is a neon number")
else:
    print(a, "not a neon number")


a=int(input("enter a number: "))
b=a+1
c=b**0.5
if c==int(c):
    print(a,"sunny number")
else:
    print(a,"not a sunny number")




a=int(input("enter a number: "))
sum=0
for i in str(a):
    sum=sum+int(i)
if a%sum==0:
    print(a,"is a harshad number")
else:
    print(a,"is not a harshad number")


a=input("enter a number: ")
b=len(a)
sum=0
for i in str(a):
    c=int(i)**b
    sum=sum+c
if int(a)==sum:
    print(a,"is a armstrong number")
else:
    print(a,"is not a armstrong number")    

a=int(input("enter a number: "))
b=a*a
length=len(str(a))
c=b%(10**length)
if a==c:
    print(a,"is automorphic")
else:
    print(a,"is not automorphic")



a=int(input("enter a number: "))
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
print(sum)
if a==sum:
    print(a,"is a perfect number")
else:
    print(a,"is not a perfect number")

a=int(input("enter a number: "))
sum=0
for i in str(a):
    fact=1
    for j in range(1,int(i)+1):
        fact=fact*j
    sum=sum+fact
print(sum)
if a==sum:
    print(a,"is a strong number")
else:
    print(a,"is not a strong number")

a=int(input("enter a number: "))
rev=0
temp=a
while a>0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
if temp==rev:
    print(temp,"palindrome")
else:
    print(temp,"not a palindrome")

n=int(input("enter a number: "))
a,b=0,1
for i in range(a,n+1):
    print(a,end=" ")
    a,b=b,a+b

a=int(input("enter a number: "))
if a<=1:
    print(a,"is not prime")
else:
    for i in range(2,a):
        if a%i==0:
            print(a,"not prime")
            break
    else:
        print("is prime")


