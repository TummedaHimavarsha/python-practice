list1=[3,22,48,5]
for i in list1:
    if i%2==0:
        print(i)
        break

for i in range(1,4):
    password=input("Enter password: ")
    if password=="crct":
        print("access granted")
        break
print("locked out")

while True:
    user=input("Enter exit if u want to stop: ")
    if user=="exit":
        break

list1=[1,-2,3,4,-5]
for i in list1:
    if i>0:
        print(i)
        continue

a="education"
for i in a:
    if i in "aeiou":
        continue
    print(i)

for i in range(1,51):
    if i%5!=0:
        continue
    elif i%3==0:
        print(i)

for i in range(1,6):
    pass

for i in list(range(81)):
    if i%2!=0:
        continue
    elif i>50:
        break
    elif i==0:
        pass
    else:
        print(i)

input=["hi","cat","wait","dog","end","zebra"]
for i in input:
    if len(i)<3:
        continue
    elif i=="end":
        break
    elif i=="wait":
        pass
    else:
        print(i)