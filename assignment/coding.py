list1=[1,2,2,3]
list2=[]
for i in list1:
    if i not in list2:                                                  
        list2.append(i)
print(list2)

a=[1,222,333]
max=a[0]
for i in a:
    if i>max:
        max=i
max2=a[0]
for j in a:
    if j>max2 and j!=max:
        max2=j
print(max2)

list1=[111,22,32]
print(sorted(list1,key=lambda x:x))

list1=[1,2,3]
list2=[4,5,6]
print(list1+list2)

list1=[1,2,3,4,5]
list2=[2,3,5]
for i in list1 and list2:
    if i in list1 and i in list2:
        print(i,end="")

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a*b/gcd(a,b)
print(gcd(12,18))
print(lcm(12,18))

list=[1,2,3]
list=list+[4]
print(list)

a="hiMa"
b=[]
for i in a:
    if i in i.upper():
        b.insert(0,i)
    else:
        b.append(i)
for i in b:
    print(i,end="")

n=int(input("enter the number of stars:"))
for i in range(1,6):
    print(" "*(6-i),end=" ")
    print("* "*i)
for j in range(6,0,-1):
    print(" "*(6-j),end=" ")
    print("* "*j)


for i in range(1,11,2):
    print(" "*(11-i),end="")
    print("* "*i)
for j in range(9,0,-2):
    print(" "*(11-j),end="")
    print("* "*j)

for i in range(1,9,2):
    print(" "*(9-i),end=" ")
    print("* "*i)
for j in range(9,0,-2):
    print(" "*(9-j),end=" ")
    print("* "*j)

a="hiMaVarsha"
b=[]
for i in a:
    if i in i.upper():
        b.insert(0,i)
    else:
        b.append(i)
for j in b:
    print(j,end=" ")

a="hiMaVarsha"
b=""
for i in a:
    if 'A'<=i<='Z':
        b=i+b
    else:
        b=b+i
print(b)

a=[2023425,999,1988]
max=a[0]
for i in a:
    if i>max:
        max=i
max2=0
for j in a:
    if j>max2 and j!=max:
        max2=j
print(max2)


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

a=[1,2,2,23,23,4,5,1,2]
b=[]

for i in a:
    if i not in b:
        b.append(i)
b.sort()
print(b)

a=[1,2,2,23,23,4,5,1,2]
b=[]

for i in a:
    if i not in b:
        b.append(i)

a=[("a","ccc","dddd","bb")]
b=[]
for i in a:
    if len(i)<a:
        b.insert(0,i)
    else:
        b.append(i)
print(b)

a=[22,333,111]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)

def maximum():
    a=[222,33,12,55]
    max=a[0]
    for i in a:
        if i>max:
            max=i
    max2=0
    for j in a:
        if j>max2 and j!=max:
            max2=j
    print(max2)
maximum()


a="moveMENT"
b=""
for i in a:
    if 'A'<=i<='Z':
        b=i+b
    else:
        b=b+i
print(b)

b=[]
for i in a:
    if i in i.upper():
        b.insert(0,i)
    else:
        b.append(i)
for j in b:
    print(j,end="")

for i in range(1,9,2):
    print(" "*(9-i),end=" ")
    print("* "*i)
for j in range(9,0,-2):
    print(" "*(9-j),end=" ")
    print("* "*j)


word=["a","cccc","ddd","bb"]
for i in range(len(word)):
    for j in range(i+1,len(word)):
        if len(word[i])>len(word[j]):
            word[i],word[j]=word[j],word[i]
print(word)

a=10
b=20
x,y=a,b
while y!=0:
    x,y=y,x%y
gcd=x
lcm=(a*b)/gcd
print(gcd)
print(lcm)

a="hima"
rev=""
for i in a:
    rev=i+rev
print(rev)

a=[1,2,4,5]
n=5
for i in range(1,n+1):
    if i not in a:
        print(i)

a=[1,2,4,5,7]
n=7
for i in range(1,n+1):
    if i not in a:
        print(i)

a=[1,2,2,4,4]
repeat=[]
for i in range(1,len(a)):
    c=a.count(i)
    if c>=2:
        repeat.append(i)
print(repeat)

a="carrac"
rev=""
for i in a:
    rev=i+rev
if a==rev:
    print("palindrome")
else:
    print("not a palindrome")

a="aeiouhm"
c=0
b=0
for i in a:
    if i in "aeiou":
        c=c+1
    else:
        b=b+1
print(f"the vowels count in the given word is {c} and the consonants count is {b}")



a="himavarsha"
b=""
c=0
for i in a:
    if i not in b:
        b=b+i
print(b)


def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

fact=1
for i in range(1,5):
    fact=fact*i
print(fact)

n=int(input("enter a number: "))
for i in range(2,n+1):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i,end=" ")

def fibs(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibs(n-1)+fibs(n-2)
for i in range(1,9):
    print(fibs(i),end=" ")
print(fibs(8))


a=1
b=20
x,y=a,b
while y!=0:
    x,y=x,x%y
gcd=x
print(gcd)
lcm=a*b/gcd
print(lcm)

for i in range(1,6):
    print(" "*(6-i),end="")
    print("* "*i)


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(1,9):
    print(" "*(9-i)+"*"*i)

for j in range(1,6):
    print(" "*(6-j),end=" ")
    print("* "*j)
for i in range(6,0,-1):
    print(" "*(6-i)+" *"*i)

for i in range(6,0,-1):
    print(" "*(6-i)+"*"*i)

a=[1,2,4]
n=5
for i in range(1,n+1):
    if i not in a:
        print(i)

a=12345
sum=0
while a>0:
    digit=a%10
    sum=sum+digit
    a=a//10
print(sum)

a=[1,2,3,4,5,6]
sum=0
for i in a:
    sum=sum+i
print(sum)

a=[1,2,2,3,3,3]
b=[]
for i in range(len(a)):
    count=a.count(i)
    if count>=2:
        b.append(i)
print(b)

a=32371
b=len(str(a))
sum=0
for i in str(a):
    c=int(i)**b
    sum=sum+c
if a==sum:
    print("arm strong")
else:
    print("not a arm strong")

a=371
sum=0
b=len(str(a))
while a>0:
    digit=a%10
    sum=sum+digit**b
    a=a//10
print(sum)




