a=int(input("enter a number"))
length=len(a)
n=len
first=n[0]
last=n[-1]
middle=n[1:-1]
sum_of_middle=sum(middle)
first_last=first+last
if first_last==sum_of_middle:
    print("first and last are equal to the sum of middle")
else:
    print("first and last are not equal to the sum of middle")