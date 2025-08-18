string=input("enter a string or a number:")
length=len(string)
if length%2==0:
    middle1=length//2-1
    middle2=length//2
    print(string[middle1]+string[middle2])
else:
    middle=length//2
    print(string[middle])
    