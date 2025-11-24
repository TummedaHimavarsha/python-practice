# a=1110
# b=220
# c=30
# if a>b and a>c:
#     print("a is the greatest")
# elif b>a and b>c:
#     print("b is the greatest")
# elif c>a and c>b:
#     print("c is the greatest")

# a=-1
# b=0
# c=30
# if a<b and a<c:
#     print("a is the smallest")
# elif b<a and b<c:
#     print("b is the smallest")
# elif c<a and c<b:
#     print("c is the smallest")


# side1=10
# side2=10
# side3=10
# if side1==side2==side3:
#     print("equilateral")
# elif side1==side2 or side2==side3 or side1==side3:
#     print("isosceles")
# elif side1!=side2!=side3:
#     print("scalene")
# else:
#     print("sorry this is it a traingle ")

# a=153
# temp=a
# sum=0
# while a>0:
#     digit=a%10
#     sum=sum+digit**3
#     a=a//10
# print(sum)
# if sum==temp:
#     print("arm strong")
# else:
#     print("not a arm strong")

#45


# num=int(input("enter a number: "))
# if num>0:
#     print("nonzero")
# elif num==0:
#     print("zero")
# else:
#     print("negative")


# num=int(input("enter a number: "))
# if num==1:
#     print("sunday")
# elif num==2:
#     print("monday")
# elif num==3:
#     print("tuesday")
# elif num==4:
#     print("wednesday")
# elif num==5:
#     print("thursday")
# elif num==6:
#     print("friday")
# elif num==7:
#     print("saturday")
# else:
#     print("please enter a proper day number")


#48

# marks=int(input("enter the marks that you have secured in the last sem: "))
# income=int(input("enter your parents income per annum: "))
# if income<=200000:
#     if marks>92:
#         print("your  eligible for scholar ship")
#     else:
#         print("score more than 92 to get scholarship")
# else:
#     print("sorry you are not eligible")


# age=18
# driving="yes"
# if driving=="yes":
#     if age>=18:
#         print("your are eligible to get a license")
#     else:
#         print("age should be >=18")
# else:
#     print("learn driving and visit again 😊")


# a=10
# b=20
# c=input("enter the operator to perform: ")
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=="*":
#     print(a*b)
# elif c=="/":
#     print(a/b)
# elif c=="//":
#     print(a//b)
# elif c=="%":
#     print(a%b)
# elif c=="**":
#     print(a**b)
# else:
#     print("please enter a operator")

# age=19
# nationality="indian"
# if age>18:
#     if nationality=="indian":
#         print("eligible to vote")
#     else:
#         print("your not a indian citizen")
# else:
#     print("your not eligible to vite becoz your age is below 18")

#53

#54

#55

# a="racecar"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)
# if a==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

# marks=int(input("enter the score: "))
# if marks>90:
#     print('A grade')
# elif marks>75:
#     print("'B' grade")
# elif marks>60:
#     print("C grade")
# else:
#     print("Fail")

# employee=int(input("enter the experience: "))
# if employee>6:
#     print("senior")
# elif employee>4:
#     print("intermediate")
# elif employee<=1:
#     print("fresher")
# else:
#     print("not a employee")

# side=int(input("enter the no of sides: "))
# if side==3:
#     print("triangle")
# elif side==4:
#     print("square or a rectangle")
# else:
#     print("circle")

# s=10
# s2=3
# s3=1
# formula=s2**2+s3**2
# if s==formula:
#     print("right angle")
# else:
#     print("not a right angle")

# a=12
# if a%5==0 or a%2==0:
#     print("the number is either divisible by 5 or  even number")
# else:
#     print("the number is not divisible by 5 and it is odd number")


# temp=int(input("enter the temperature: "))
# if temp>120:
#     print("hot")
# elif temp==90:
#     print("normal")
# elif temp<30:
#     print("low")

# age=13
# marks=99
# if age>12:
#     if marks>90:
#         print("admission seat will be alloted")
#     else:
#         print("try for good marks next time")
# else:
#     print("your age needs to be >12")

# product=input("enter the name of the product to view tthe ratings: ")
# if product=="mamaearth":
#     print("⭐⭐⭐")
# elif product=="maybelline":
#     print("⭐⭐⭐⭐⭐")
# elif product=="lakme":
#     print("⭐⭐⭐⭐")
# elif product=="blabla":
#     print("⭐")
# else:
#     print("enter a valide name")

# original=1000
# soldamount=15000
# if soldamount>1000:
#     print("profit")
# else:
#     print("loss")

# a="20"
# lens=len(a)
# if lens==2:
#     print("2 digit number")
# else:
#     print("not a 2 digit number")

# marks=int(input("enter the score: "))
# if marks>90:
#     print('A grade')
# elif marks>75:
#     print("'B' grade")
# elif marks>60:
#     print("C grade")
# else:
#     print("Fail")

#70

# marks=int(input("enter the score: "))
# if marks>90:
#     print('A grade')
# elif marks>75:
#     print("'B' grade")
# elif marks>60:
#     print("C grade")
# else:
#     print("Fail")

#72

# color=input("enter the color: ")
# if color=="red":
#     print("stop")
# elif color=="yellow":
#     print("ready to go")
# elif color=="green":
#     print("Go")
# else:
#     print("color out of range")

num=int(input("enter a number: " ))
if 10<num<20:
    print("in the range")
else:
    print("out of range")    