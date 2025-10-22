a=[i for i in range(1,21) if i%2!=0]
print(a)

cubes=print({i:i**3 for i in range(1,11)})

word="programming in python"
vowels=print({i for i in word if i in "aeiou"})

d={'a':1,'b':2,'c':3}
print({d[i]:i for i in d })
print({i:j for j,i in d.items()})

n=5
t=print(tuple(n*i for i in range(1,6)))

l=[-3,-1,0,2,4,-6]
a=print([i for i in l if i>=0])

a="python is"
b=print({i:j for i in a for j in i})

a=print(["even" if i%2==0 else "odd" for i in range(1,11) ])

a=print(tuple(i*i for i in range(1,8)))

list1=[1,2,2,3,4,4,5,5,6]
a={i for i in list1}
print(list(a))

a={'a':1,'b':2,'c':3}
print({i:j for j,i in a.items()})

a=[[i for i in range(0,3)] for j in range(0,5)]
print(a)

a=[[1,2,3],[3,4,5]]
b=print({j for i in a for j in i})
c=print([(x,y) for x in [1,2,3] for y in [3,4,5]])
d=print({j for i in a for j in i if j%2!=0})


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


for i in range(1,4):
    for j in range(1,7):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()

for i in range(1,6):
    print(" " *(6-i)+'*'*i)

for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(' ',end=' ')
    print()

for i in range(1,4):
    for j in range(1,7):
        print(j,end=" ")
    print()

for i in range(1,6):
    print(" "*(6-i),end=" ")
    print("* "*i)

for i in range(6,0,-1):
    print(" "*(6-i),end=" ")
    print("* "*i)

for i in range(1,6):
    print(" "*(6-i),end=" ")
    print("* "*i)
for j in range(6,0,-1):
    print(" "*(6-j),end=" ")
    print("* "*j)