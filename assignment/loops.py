i=1
while i<5:
    print(i)
    i=i+1
print(i)

i=1
while i<=10:
    if i%2==0:
        print(i)
    i=i+1

i=1
sum=0
while i<=10:
    sum=sum+i
    i=i+1
print(sum)

i=123
while str(i):
    print(i)

i=10
while i>=1:
    print(i)
    i=i-1

for i in range(1,11):
    print(i)

a="banana"
for i in a:
    print(i)
    
for i in range(1,6):
    a=i*i
    print(a)

list=[2,5,8,9,10]
for i in list:
    if i%2==0:
        print(i)

for i in range(1,21):
    if i%3==0:
        print(i)

for i in range(1,4):
    for j in range(1,i+1):
        print("*",end=" ")
    print( )

for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print( )
    
for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=" ")
    print( )

b=2
for i in range(1,11):
    a=i*b
    print(f"{b}*{i}={a}")

words=["hi","ok"]
for i in words:
    for j in i:
        print(j)

for i in range(1,11):
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")

word="hima"
count=0
for i in word:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        print(i)


word="himavarsha"
for i in word:
    count=0
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count=count+1
        print(count,i)

for i in range(1,6):
    print("hello")

for i in range(1,4):
    user=input("enter ur fav color: ")

ab="banana"
count=0
for i in ab:
    if i=="a":
        count=count+1
print(count)

a="banana"
print(a.count("a"))

for i in range(1,11):
    if i<5:
        print(i,"small")
    else:
        print(i,"big")



