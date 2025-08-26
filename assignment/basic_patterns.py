for i in range(1,4):
    print("*",end=" ")
for i in range(1,4):
    print("*",end="")
for i in range(1,4):
    print("*",end="5")

for i in range(1,4):
    for j in range(1,6):
        print("*",end=" ")
    print() #rectangle

for i in range(1,4):
    for j in range(1,4):
        print("*",end=" ")
    print() #square

for i in range(1,6):
    for j in range(1,4):
        print("*",end=" ")
    print()# vertical rectangle

#right angle triangle
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


for row in range(6,0,-1):
    for column in range(0,row):
        print("*",end=" ")
    print()




