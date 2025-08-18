age=int(input("enter your age:"))
if age>=18:
    license=input("do you have license?")
    if license=="yes":
        print("eligible to drive")
    else:
        print("go and get license")
else:
    print("minor")

"""
age=int(input("enter your age:"))
license=input("do you u have license :")
if age>=18 and license=="yes":
    print("eligible to drive")
else:
        print("go and get license and you are a minor")"""