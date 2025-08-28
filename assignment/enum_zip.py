fruits = ["apple", "banana", "cherry"]
for i,j in enumerate(fruits,start=200):
    print(i," ",j)

students = ["Alice", "Bob", "Charlie"]
for i in enumerate(students,start=1):
    print(i)

colors = ["red", "green", "blue"]
for i,j in enumerate(colors):
    print(i,j)

languages = ["java", "c++", "python", "ruby"]
for index,langs in enumerate(languages):
    if langs=="python":
        print("index of python is:",index)

a="hello"
for i,j in enumerate(a):
    print(i,j)

#zip



names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]
for i,j in zip(names,marks):
    print(i,j)


names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]
combo=(zip(names,marks))
for i in combo:
    print(i)


names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]
for i,j in zip(names,marks):
    print(i,"scored",j)

pairs = [("a", 1), ("b", 2), ("c", 3)]
combo=(zip(*pairs))
for i in combo:
    print(i)

ids = [101, 102, 103]
names = ["Tom", "Jerry", "Mickey"]
grades = ["A", "B", "A"]
combo=(zip(ids,names,grades))
for i in combo:
    print(i)


a = [1, 2, 3, 4]
b = ["x", "y"]
c=(zip(a,b))
for i in c:
    print(i)