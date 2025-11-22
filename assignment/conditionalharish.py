num=int(input("Enter a number: "))
if num>0:
    print("The number is positive.")
elif num==0:
    print("The number is zero.")
else:
    print("The number is negative.")

num=int(input("enter a number:"))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

num=int(input("enter a number:"))
num1=int(input("enter a number:"))
if num>num1:
    print(f"{num} is the greatest number")
else:
    print(f"{num} is the smallest number")

num=int(input("enter a number:"))
num1=int(input("enter a number:"))
if num<num1:
    print(f"{num} is smaller than {num1}")
else:
    print(f"{num} is greater than {num1}")

year=int(input("enter the year: "))
if year%400==0 or year%4==0 and year%100!=0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

num=int(input("enter a number:"))
if num%5==0:
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 5")

num=int(input("enter a number:"))
if num%5==0 and num%3==0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by 3 or 5")

num=int(input("enter a number:"))
if 1<=num<=100:
    print(f"{num} is the number that exists between 1 and 100")
else:
    print(f"{num} is the number that does not exists between 1 and 100")

str="l"
if str in "aeiou":
    print(f"{str} is a vowel")
else:
     print(f"{str} is not a vowel")

num="hima"
if num.isdigit():
    print("yes")
else:
    print("false")

number="1"
lens=len(number)
# print(lens)
if lens>1:
    print("The given number is not single digit")
else:
    print(f"{number} is single digit")

age=19
if age>18:
    print("eligible to vote")
else:
    print("not eligible")

num=int(input("enter a number:"))
if num%2 and num%3==0:
    print("number is divible by either 2 or 3")
elif num%2==0:
    print("number is divisible by 2")
elif num%3==0:
    print("number is divisible by 3")
else:
    print("number is neither divisible by 2 or 3")


num=int(input("enter a number:"))
if num%7==0 and num%5!=0:
    print("The number is divisible by 7 and not by 5")
else:
    print("None")

15 th question

a=22
b=21
if a>b:
    print(a)
else:
    print(b)

marks=int(input("enter the score: "))
if marks>90:
    print('A grade')
elif marks>75:
    print("'B' grade")
elif marks>60:
    print("C grade")
else:
    print("Fail")

num=int(input("enter a number:" ))
if 10<=num<=20:
    print(num)
else:
    pass

num=int(input("enter a number:" ))
if 10<=num<=20:
    pass
else:
    print(num)

20 th question


num=int(input("enter a number:" ))
if num%10==0:
    print("the given number is multiple of 10")
else:
    print("the given number is not multiple of 10")

age=int(input("enter the age: "))
if age<10:
    print("child")
elif age<=19:
    print("teenager")
else:
    print("adult")

num="133"
lens=len(num)
if len(num)==3:
    print("the given number is 3 digit")
else:
    print("the given number is not 3 digit")

age=21
age2=19
if age>age2:
    print(f"{age} is elder")
else:
    print(f"{age} is younger")


num=int(input("enter a number: "))
if num<1000:
    if num%11==0:
        print("The given number is divisible by 11")
    else:
        print("Thenumber is not divisible by 11")
else:
    print("Sorry the number is not less than 1000")

a=10
b=20
num=int(input("enter a number: "))
if a<num<b:
    print("yes")
else:
    print("no")

a=10
b=21
if a%2==0 and b%2==0:
    print("both are even")
else:
    print("not even")

num=int(input("enter a number: "))
if num>0:
    print("nonzero")
elif num==0:
    print("zero")
else:
    print("negative")

side1=10
side2=11
side3=10
if side1==side2==side3:
    print("It is a triangle")
else:
    print("it is not a trinagle")

num=int(input("enter the month number: "))
if num==1 or num==2 or num==12:
    print("winter")
elif num==3 or num==4 or num==5:
    print("summer")
elif num==6 or num==7 or num==8 or num==9:
    print("rainy")
elif num==10 or num==11:
    print("autumn")
else:
    print("invalid month number")

32 question 

num=int(input("enter the number: "))
a=num**0.5
print(a)
if a==int(a):
    print("the given number is a perfect square")
else:
    print("the given number is not a perfect square")

num=int(input("enter a number: "))
if num==1:
    print("sunday")
elif num==2:
    print("monday")
elif num==3:
    print("tuesday")
elif num==4:
    print("wednesday")
elif num==5:
    print("thursday")
elif num==6:
    print("friday")
elif num==7:
    print("saturday")
else:
    print("please enter a proper day number")

35 question

36

num=int(input("enter a number: "))
if num%9==0 and num%6!=0:
    print("divisible by 9 but not 6")
else:
    print("no")


38

marks=int(input("enter the score: "))
if marks>90:
    print('A grade')
elif marks>75:
    print("'B' grade")
elif marks>60:
    print("C grade")
else:
    print("Fail")

a=20
b=20
c=20
if a==b==c:
    print("all are equal")
else:
    print("not equal")


