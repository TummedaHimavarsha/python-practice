a=lambda x:"even" if x%2==0 else "odd"
print(a(0))

ab=lambda a,b:a if a>b else b
print(ab(10,2))

a=lambda x:x*x
print(a(5))

list1=[1,2,3,4,5,6,8,10]
a=print(list(filter(lambda x:x%2==0,list1)))

from functools import reduce
list=[1,2,3]
a=print(reduce(lambda x,y:x*y,[1,2,3]))

a=[(1,31),(8,9),(10,11)]
result=print(list(sorted(a,key=lambda x:x[1])))

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(6))

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(5))

def rev(n):
    if n=="":
        return n
    else:
        return rev(n[1::])+n[0]
print(rev("hima"))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(9):
    print(fib(i),end=" ")

def sum(n):
    if n==0:
        return 0
    else:
        return (n%10)+sum(n//10)
print(sum(12345))

def power(base,exp):
    if exp==0:
        return 1
    else:
        return base*power(base,exp-1)
print(power(2,5))