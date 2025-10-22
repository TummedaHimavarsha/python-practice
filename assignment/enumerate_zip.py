fruits=["apple","banana","cherry"]
for i,j in enumerate(fruits,start=101):
    print(i,j)

students = ["Alice", "Bob", "Charlie"]
for i,j in enumerate(students,start=1):
    print(i,j)

colors=["red","green","blue"]
for i,j in enumerate(colors,start=10):
    print(i,j)

colors=["red","green","blue"]
c=0
for i in colors:
    print(c,i)
    c=c+1

languages = ["java", "c++", "python", "ruby"]
for i,j in enumerate(languages):
    if j=="python":
        print(i,j)

a="hello"
for i,j in enumerate(a):
    print(i,j)

names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]

a=zip(names,marks)
for i in a:
    print(i)

for i,j in zip(names,marks):
    print(i,"scored",j)

pairs = [("a", 1), ("b", 2), ("c", 3)]
c=zip(*pairs)
for i in c:
    print(i)

ids = [101, 102, 103]
names = ["Tom", "Jerry", "Mickey"]
grades = ["A", "B", "A"]
a=zip(ids,names,grades)
for i in a:
    print(i)

pairs = [("a", 1), ("b", 2), ("c", 3)]
for i in zip(*pairs):
    print(i)



a = [1, 2, 3, 4]
b = ["x", "y"]
for i,j in zip(a,b):
    print(i,j)