a=int(input("enter a number: "))
if a%3==0 and a%5==0:
    print("divisible by both 3 and 5")
else:
    print("not divisible")

a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a>b:
    print(f"{a} is greater")
else:
    print(f"b is greater")

score=int(input("enter your score: "))
if score>=90:
    print("Grade A")
elif score>=70:
    print("Grade B")
elif score>=60:
    print("Grade C")
else:
    print("Fail")

a=int(input("enter a number: "))
if a>0:
    print(f"{a} is positive number")
else:
    print(f"{a} is negative number")

age=int(input("enter your age: "))
if age>=20:
    print("Adult")
elif age==13 or age==19:
    print("teen")
elif age<13:
    print("child")

