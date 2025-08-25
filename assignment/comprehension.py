a=[1,2,3]
b=[4,5,6]
c=a+b
list=tuple(c)
print(list)

c=[list for i in list]


a=[i for i in range(1,11)]
print(a)

a=[i*i for i in range(1,11)]
print(a)

list=[2,3,4,5,6,7,8]
list1=[]
a=[list1.append(i) for i in list if i%2!=0]
print(list1)

a="python"
list=[]
l=[list.append(i) for i in a]
print(list)


list=[]
a=[list.append(i) for i in range(1,21) if i%3==0]
print(list)

list=["apple","banana","cherry","kiwi","mango"]
list1=[]
for i in list:
    if len(i)>5:
        list1.append(i)
print(list1)

list=["apple","banana","cherry","kiwi","mango"]
list1=[]
a=[i for i in list if len(i)>5]
print(a)
a=[i.upper() for i in list]
print(a)
for i in list:
    a=i[0]
    list1.append(a)
print(list1)
a=[i[0] for i in list]
print(a)



list=[]
for i in range(1,11):
    a=i**3
    if i%2!=0:
        list.append(i)
print(list)

list=[]
a=[i**3 for i in range(1,11) if i%2!=0]
print(a)

list=[[1,2],[3,4],[5,6]]
list1=[]
for i in list:
    for j in i:
        list1.append(j)
print(list1)

a=[j for i in list for j in i]
print(a)

a="comprehensions are powerful"
list=[]
for i in a:
    if i in "aeiou":
        list.append(i)
print(list)

a="comprehensions are powerful"
list=[]
b=[list.append(i) for i in a if i in "aeiou"]
print(list)


dict={}
for i in range(1,6):
    dict[i]=i*i
print(dict)


a={i:i*i for i in range(1,6)}
print(a)

list= ["apple", "banana", "cherry", "kiwi", "mango"]
list1=[]
for i in list:
    if "a" in i:
        list1.append(i)
print(list1)


a=[i for i in list if "a" in i]
print(a)


