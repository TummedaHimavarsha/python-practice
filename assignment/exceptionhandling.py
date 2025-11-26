try:
    num=int(input("Enter a number: "))
    result=10/num
    print(result)
except:
    print("something went wrong")

try:
    num=int(input("Enter a number: "))
    result=10/num
except ZeroDivisionError as e:
    print(e)


try:
    a=int("hima")
    print(a)
except ValueError as e:
    print(e)

try:
    print(a)
except NameError as e:
    print(e)

try:
    list=[1,2,3]
    print(list[3])
except IndexError as error:
    print(error)

try: 
    dic={"name":"Himavarsha"}
    print(dic["age"])
except KeyError as e:
    print(e) #wdefsrdgfhndfghjfgggggggggggggggggggggg

try:
    a=1
    b="hima"
    print(a+b)
except TypeError as e:
    print(e)


try:
    open("abc.txt")
except FileNotFoundError as e:
    print(e)

try:
    a=int(input("enter a number: "))
    result=a/0
    print(result)
except ValueError:
    print("wrong value")
except ZeroDivisionError as e :
    print(e)

try:
    list=[1,2,3]
    sum=0
    for i in list:
        sum=sum+{i}
    print(sum)
except Exception as e:
    print(e)
finally:
    print("Program End")



try:
    print("hello")
except Exception as e:
    print(e)
else:
    print("No Error Found")


try:
    a=int(input("enter a number: "))
    reult=a/0
    print(reult)
except (ValueError,ZeroDivisionError) as e:
    print(e)

try:
    open("file.txt")
except FileNotFoundError:
    print("The file ur trying to access is not exisiting")

try:
    open("file.txt")
except FileNotFoundError:
    print("The file ur trying to access is not exisiting")
finally:
    print("the file is closed safely")


try:
    a=int(input("enter a number: "))
    reult=a/0
    print(reult)
except (ValueError,ZeroDivisionError) as e:
    print(e)

try:
    a=int(input("enter a number: "))
    print(a)
except ValueError as e:
    print(e) #dddddddddddddddddddddddddddddd

a=10
assert a<0,("a is positive")
print("done")

class AgeError(Exception):
    pass
try:
    age=int(input("enter your age: "))
    if age<0:
        raise AgeError("age should be greater than 0")
except AgeError as e:
    print(e)

class passwordError(Exception):
    pass
try:
    password=input("enter: ")
    if len(password)<5:
        raise passwordError("password is too short")
except passwordError as e:
    print(e)

try:
    a=10/0 #zero
    b=10+"hima" #Type error
    c=int("hima") #value error
    print(d) #name error
    e={"name":"himavarsha"}
    print(e["age"]) #key error
    lis1=[1,2,3]
    print(lis1[4])#index error
    open("file.txt") #filenotfound error 
except Exception as e:
    print(e)

