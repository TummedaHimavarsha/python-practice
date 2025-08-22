a=371
sum=0
for i in str(a):
    b=int(i)
    c=b**3
    sum=sum+c
print(sum)
if sum==a:
    print("armstrong number")
else:
    print("not a arm strng number")

    

for i in range(1,1001):
    sum=0
    for j in str(i):
        a=int(j)
        b=a**3
        sum=sum+b
    if sum==i:
        print(i)
        

a=int(input("enter a number: "))
b=int(input("enter a number: "))
total=0
for i in range(a,b+1):
    sum=0
    for j in str(i):
        a=int(j)
        b=a**3
        sum=sum+b
        x=0
    if sum==i:
        total+=i
print(total)
        
