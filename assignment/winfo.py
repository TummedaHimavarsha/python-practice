str="hima"
rev=""
for i in str:
    rev=i+rev
print(rev)

li=[1111,33,222]
max=li[0]
for i in li:
    if i>max:
        max=i
print(max)

a="himavarsha"
c=0
for i in a:
    if i in "aeiou":
        c+=1
print(c)

def pal(str):
    if len(str)<=1:
        return True
    elif str[0]!=str[-1]:
        return False
    else:
        return pal(str[1:-1])
print(pal("madam"))

a=10
b=20
x,y=a,b
while y!=0:
    x,y=y,x%y
gcd=x
lcm=(a*b)/gcd
print(lcm,gcd)

a,b=0,1
for i in range(1,6):
    print(a,end=" ")
    a,b=b,a+b

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(9):
    print(fib(i),end=" ")

li=[1,2,2,4,5,8,8]
b=[]
for i in li:
    if i not in b:
        b=b+[i]
print(b)

a="himavarsha"
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

a=open("porsche.txt","r")
b=a.readlines()
print(b)


a=open("porsche.txt","w")
a.write("hello")


a=open("porsche.txt","a")
a.writelines(["a\n","b\n"])
print(a.closed)
a.close()
print(a.closed)

import json
data=[1,2,3,4,5]
with open("porsche.txt","w") as f:
    json.dump(data,f,indent=4)

li=[222,33333,1111]
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if len(str(li[i]))>len(str(li[j])):
            li[i],li[j]=li[j],li[i]
print(li)


a="ate"
b="eat"
if len(a)!=len(b):
    print("not anagrams")
else:
    for i in a:
        if a.count(i)!=b.count(i):
            print("not anagrams")
            break
    else:
        print("anagrams")

dict1={1:"1",2:"2",3:"3"}
dict2={4:"4",5:"5",6:"6"}
dict1.update(dict2)
print(dict1)           


a=[i for i in range(1,11) if i%2==0]
print(a)

try:
    a=10/0
    print(a)
except ZeroDivisionError as e:
    print(e)

list1=[1,2,3]
list2=[2,4,5]
ist3=[]
for i in list1:
    if i in list2:
        ist3=ist3+[i]
print(ist3)


