for i in range(1,51):
    if i%3==0:
        continue
    print(i)


while True:
    user=int(input("enter  a number: "))
    if user%11==0:
        print(f"{user} is divisible by 11")
        break

a="himavarsha"
count=0
for i in a:
    if i in "aeiou":
     count+=1
print(count)

i=100
while i>1:
    if i%2==0:
        print(i)
    i=i-1

while True:
    user =input("enter ur password: ")
    if user=="admin123":
        print("valid credentials")
        break

a=int(input("enter a number: "))
for i in range(1,11):
    print(f'{a} * {i} = {a*i}')

i=1
while i<10:
    user=int(input("enter  a number :"))
    if user<0:
        continue
    else:
        print(i)
    i=i+1

for i in range(1,11):
    user=int(input("enter  a number :"))
    if user<0:
        continue
    else:
        print(i)

n=int(input("enter  a number :"))
sum=0
for i in range(1,n+1):
    if i%2!=0:
        sum=sum+i
print(sum)



for i in range(0,50):
    if i<=1:
        print("not prime")
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,"prime")

sum=0
while True:
    num=int(input("enter a number: "))
    sum=sum+num
    if num==0:
        print(sum)
        break
