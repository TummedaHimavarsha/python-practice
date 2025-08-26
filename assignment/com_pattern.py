num=[]
for i in range(1,21):
    a=i*i
    num.append(a)
print(num)

a=[i*i for i in range(1,21)]
print(a)

a={i:i**3 for i in range(1,11)}
print(a)

str="programming in python"
a={i for i in str}
print(a)

n=int(input("enter a number: "))
a=tuple(n*i for i in range(1,11))
print(tuple(a))

nums=[-3,-1,0,2,4,-6]
n=[]
for i in nums:
    if i>=0:
        n.append(i)
print(n)

nums=[-3,-1,0,2,4,-6]
a=[i for i in nums if i>=0]
print(a)


word=["python","makes","coding","easier"]
a={i:len(i) for i in word}
print(a)

eve=[]
for i in range(1,11):
    if i%2==0:
        eve.append("even")
    else:
        eve.append("odd")
print(eve)

a=["even" if i%2==0 else "odd" for i in range(1,11)]
print(a)

a=tuple(i*i for i in range(1,8))
print(tuple(a))


num=[1,2,2,3,4,4,5,5,6]
new=[]
for i in num:
    if i not in new:
        new.append(i)
print(new)

num=[1,2,2,3,4,4,5,5,6]
new=[]
a=[new+i for i in num if i not in new]
print(a)

d = {'a': 1, 'b': 2, 'c': 3}
reverse={v:k for k,v in d.items()}
print(reverse)



for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


for i in range(1,4):
    for j in range(1,7):
        print(j,end=" ")
    print()


for i in range(6,0,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()

