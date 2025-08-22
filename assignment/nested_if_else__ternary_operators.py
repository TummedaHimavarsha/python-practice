bottles=int(input("enter the count of bottles: "))
amount=25
if bottles>=2:
    a=15/100*amount
    print(a)
else:
    b=5/100*amount
    print(b)


type=input("enter which type of vehicle is yours: ")
fuel=int(input("enter the fuel percentage: "))
if fuel<=25:
    if type=="car":
        print("refuel soon at a petrol station")
    elif type=="bike":
        print("refuel at nearest pump")
    else:
        print("Check vehicle type")

grade=int(input("enter ur score :"))
income=int(input("enter ur income :"))
if grade>85:
    if income<300000:
        print("eligible for scholarship")
    elif 300000<income<600000:
        print("eligible for half scholarship")
    else:
        print("No scholarship")
else:
    print("get >85 marks")

cartvalue=int(input("enter the value: "))
paymenttype=input("enter the payment mode: ")
if cartvalue>1000:
    if paymenttype=="card":
        a=cartvalue*10/100
        b=cartvalue-a
        print(f"the total amount after 10% discount is {b}")
    elif paymenttype=="UPI":
        c=cartvalue*15/100
        d=cartvalue-c
        print(f"the total amount after 10% discount is {d}")
else:
    print("no discount")

age=int(input("enter ur age: "))
vaccinated=input("enter ur vaccinated or not: ")
if age>=18:
    if vaccinated=="vaccinated":
        print("Allowed to dine in")
    elif  vaccinated=="not vaccinated":
        print("Takeaway only")
else:
    print("u must be atleast 18 to dine here")


age=int(input("enter ur age: "))
height=int(input("enter ur height: "))
if 14<=age<=18:
    if height>=160:
        print("eligible")
    else:
        print("not eligible")
else:
    print("age out of range")

ternary operator problems

light=input("enter the color: ")
print("Go" if light=="green" else "Stop")

age=int(input("enter ur age: "))
print("Adult ticket" if age>=18 else "Child ticket")

amount=int(input("enter the amount spent: "))
print("you get a free gift" if amount>=500 else "No gift")

location=input("enter if local or not: ")
print("20$ delivery fee" if location=="local" else "50$ delivery fee")

temp=int(input("enter the temperature: "))
print("High fever" if temp>=100 else "Normal")

time=int(input("enter the time: "))
print("Good morning" if time<=12 else "Good afternoon" if time<=17 else "Good evening")

units=int(input("enter the units"))
if units<100:
    print("Free")
elif 100<=units<=300:
    usage=input("enter residential or commercial: ")
    if usage=="residential":
        print(f"5$ per unit: {units+5}")
    else:
        print(f"8$ per unit: {units+8}")
if units>300:
    print(f"10$ per unit flat {units-8}")
        

