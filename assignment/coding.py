# list1=[1,2,2,3]
# list2=[]
# for i in list1:
#     if i not in list2:                                                  
#         list2.append(i)
# print(list2)

# a=[1,222,333]
# max=a[0]
# for i in a:
#     if i>max:
#         max=i
# max2=a[0]
# for j in a:
#     if j>max2 and j!=max:
#         max2=j
# print(max2)

# list1=[111,22,32]
# print(sorted(list1,key=lambda x:x))

# list1=[1,2,3]
# list2=[4,5,6]
# print(list1+list2)

# list1=[1,2,3,4,5]
# list2=[2,3,5]
# for i in list1 and list2:
#     if i in list1 and i in list2:
#         print(i,end="")

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# def lcm(a,b):
#     return a*b/gcd(a,b)
# print(gcd(12,18))
# print(lcm(12,18))

# list=[1,2,3]
# list=list+[4]
# print(list)

# a="hiMa"
# b=[]
# for i in a:
#     if i in i.upper():
#         b.insert(0,i)
#     else:
#         b.append(i)
# for i in b:
#     print(i,end="")

# n=int(input("enter the number of stars:"))
# for i in range(1,6):
#     print(" "*(6-i),end=" ")
#     print("* "*i)
# for j in range(6,0,-1):
#     print(" "*(6-j),end=" ")
#     print("* "*j)


# for i in range(1,11,2):
#     print(" "*(11-i),end="")
#     print("* "*i)
# for j in range(9,0,-2):
#     print(" "*(11-j),end="")
#     print("* "*j)

# for i in range(1,9,2):
#     print(" "*(9-i),end=" ")
#     print("* "*i)
# for j in range(9,0,-2):
#     print(" "*(9-j),end=" ")
#     print("* "*j)

# a="hiMaVarsha"
# b=[]
# for i in a:
#     if i in i.upper():
#         b.insert(0,i)
#     else:
#         b.append(i)
# for j in b:
#     print(j,end=" ")

# a="hiMaVarsha"
# b=""
# for i in a:
#     if 'A'<=i<='Z':
#         b=i+b
#     else:
#         b=b+i
# print(b)

# a=[2023425,999,1988]
# max=a[0]
# for i in a:
#     if i>max:
#         max=i
# max2=0
# for j in a:
#     if j>max2 and j!=max:
#         max2=j
# print(max2)


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# a=[1,2,2,23,23,4,5,1,2]
# b=[]

# for i in a:
#     if i not in b:
#         b.append(i)
# b.sort()
# print(b)

# a=[1,2,2,23,23,4,5,1,2]
# b=[]

# for i in a:
#     if i not in b:
#         b.append(i)

# a=[("a","ccc","dddd","bb")]
# b=[]
# for i in a:
#     if len(i)<a:
#         b.insert(0,i)
#     else:
#         b.append(i)
# print(b)

# a=[22,333,111]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# def maximum():
#     a=[222,33,12,55]
#     max=a[0]
#     for i in a:
#         if i>max:
#             max=i
#     max2=0
#     for j in a:
#         if j>max2 and j!=max:
#             max2=j
#     print(max2)
# maximum()


# a="moveMENT"
# b=""
# for i in a:
#     if 'A'<=i<='Z':
#         b=i+b
#     else:
#         b=b+i
# print(b)

# b=[]
# for i in a:
#     if i in i.upper():
#         b.insert(0,i)
#     else:
#         b.append(i)
# for j in b:
#     print(j,end="")

# for i in range(1,9,2):
#     print(" "*(9-i),end=" ")
#     print("* "*i)
# for j in range(9,0,-2):
#     print(" "*(9-j),end=" ")
#     print("* "*j)


# word=["a","cccc","ddd","bb"]
# for i in range(len(word)):
#     for j in range(i+1,len(word)):
#         if len(word[i])>len(word[j]):
#             word[i],word[j]=word[j],word[i]
# print(word)

# a=10
# b=20
# x,y=a,b
# while y!=0:
#     x,y=y,x%y
# gcd=x
# lcm=(a*b)/gcd
# print(gcd)
# print(lcm)

# a="hima"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a=[1,2,4,5]
# n=5
# for i in range(1,n+1):
#     if i not in a:
#         print(i)

# a=[1,2,4,5,7]
# n=7
# for i in range(1,n+1):
#     if i not in a:
#         print(i)

# a=[1,2,2,4,4]
# repeat=[]
# for i in range(1,len(a)):
#     c=a.count(i)
#     if c>=2:
#         repeat.append(i)
# print(repeat)

# a="carrac"
# rev=""
# for i in a:
#     rev=i+rev
# if a==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

# a="aeiouhm"
# c=0
# b=0
# for i in a:
#     if i in "aeiou":
#         c=c+1
#     else:
#         b=b+1
# print(f"the vowels count in the given word is {c} and the consonants count is {b}")



# a="himavarsha"
# b=""
# c=0
# for i in a:
#     if i not in b:
#         b=b+i
# print(b)


# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# fact=1
# for i in range(1,5):
#     fact=fact*i
# print(fact)

# n=int(input("enter a number: "))
# for i in range(2,n+1):
#     prime=True
#     for j in range(2,i):
#         if i%j==0:
#             prime=False
#             break
#     if prime:
#         print(i,end=" ")

# def fibs(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibs(n-1)+fibs(n-2)
# for i in range(1,9):
#     print(fibs(i),end=" ")
# print(fibs(8))


# a=1
# b=20
# x,y=a,b
# while y!=0:
#     x,y=x,x%y
# gcd=x
# print(gcd)
# lcm=a*b/gcd
# print(lcm)

# for i in range(1,6):
#     print(" "*(6-i),end="")
#     print("* "*i)


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,9):
#     print(" "*(9-i)+"*"*i)

# for j in range(1,6):
#     print(" "*(6-j),end=" ")
#     print("* "*j)
# for i in range(6,0,-1):
#     print(" "*(6-i)+" *"*i)

# for i in range(6,0,-1):
#     print(" "*(6-i)+"*"*i)

# a=[1,2,4]
# n=5
# for i in range(1,n+1):
#     if i not in a:
#         print(i)

# a=12345
# sum=0
# while a>0:
#     digit=a%10
#     sum=sum+digit
#     a=a//10
# print(sum)

# a=[1,2,3,4,5,6]
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)

# a=[1,2,2,3,3,3]
# b=[]
# for i in range(len(a)):
#     count=a.count(i)
#     if count>=2:
#         b.append(i)
# print(b)

# a=32371
# b=len(str(a))
# sum=0
# for i in str(a):
#     c=int(i)**b
#     sum=sum+c
# if a==sum:
#     print("arm strong")
# else:
#     print("not a arm strong")

# a=371
# sum=0
# b=len(str(a))
# while a>0:
#     digit=a%10
#     sum=sum+digit**b
#     a=a//10
# print(sum)

# n=10
# a,b=0,1
# for i in range(1,n+1):
#     print(a,end=" ")
#     a,b=b,a+b

# def fibs(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibs(n-1)+fibs(n-2)
# for i in range(9):
#     print(fibs(i),end=" ")

# n=10
# for i in range(2,n+1):
#     prime=True
#     for j in range(2,i):
#         if i%j==0:
#             prime=False
#             print(i,"false")
#             break
#     if prime:
#         print(i,"prime",end="")
#         print()


# a=10
# b=80
# x,y=a,b
# while y!=0:
#     x,y=y,x%y
# gcd=x
# print(gcd)
# lcm=a*b/gcd
# print(lcm)

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(10,80))
# def lcm(a,b):
#     if b==0:
#         return a
#     else:
#         return a*b//gcd(a,b)
# print(lcm(10,80))

# a="hima"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a="himavarsha"
# c=0
# b=0
# for i in a:
#     if i in "aeiou":
#         c=c+1
#     else:
#         b=b+1
# print(f"The vowels in the given string is {c}")
# print(f"The consonants in the given string are {b}")

# a=[2222,333,1]
# b=sorted(a ,key=lambda x:len(str(x)))
# print(b)
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# a="himavarsha"
# b=""
# for i in a:
#     if i not in b:
#         print(f"{i}",a.count(i))
#         b=b+i

# a="himavarsha"
# b=""
# for i in a:
#     if a.count(i)==1:
#         b=b+i
# print(b)

# for i in range(1,6,2):
#     print(" "*(6-i),end=" ")
#     print("* "*i)
# for j in range(6,0,-2):
#     print(" "*(6-j),end=" ")
#     print("* "*j)

# a=["A","B","C","D"]
# for i in range(len(a)):
#     for j in range(i+1):
#         print(a[j],end=" ")
#     print()

# letters="abcdefghijklmnopqrstuvwxyz"
# k=0
# for i in range(1,6):
#     for j in range(i):
#         print(letters[k],end=" ")
#         k=k+1
#     print()

# a="himhhavarsha"
# b=""
# for i in a:
#     if i not in b:
#         b=b+i
#     elif i in b:
#         print(i)
#         break

# def num(n):
#     if n==0:
#         return 0
#     else:
#         num(n-1)
#         print(n)
        
# print(num(5))


# a="banana"
# count={}
# for i in a:
#     if i in count:
#         count[i]=count[i]+1
#     else:
#         count[i]=1
# print(count)

# a=[1,2,3,3,5]
# miss=[]
# repeat=[]
# for i in a:
#     count=a.count(i)
#     if a.count(i)>1:
#         repeat.append(i)
# print(repeat)
# n=5
# for j in range(1,n+1):
#     if j not in a:
#         print(j)

# a=[22,11,11,333]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# for i in range(len(b)):
#     for j in range(i+1,len(b)):
#         if b[i]>b[j]:
#             b[i],b[j]=b[j],b[i]
# print(b)


# for i in range(3):
#     print(" "*(3-i),end=" ")
#     for j in range(1,i+1):
#      print(j,end=" ")
#     print(" ")
# for i in range(3,0,-1):
#     print(" "*(3-i),end=" ")
#     for j in range(1,i+1):
#      print(j,end=" ")
#     print(" ")

# a=10
# b=20
# temp=0
# temp=a
# a=b
# b=temp
# print(a,b)

# n=153
# a=len(str(n))
# sum=0
# temp=n
# while n>0:
#     digit=n%10
#     sum=sum+digit**a
#     n=n//10
# print(sum)

# n=29
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# print(sum)

# a="madam"
# rev=""
# for i in a:
#     rev=i+rev
# if a[0::]==a[-1::-1]:
#     print("palindrome")
# else:
#     print("not a a palindrome")

# n=10
# a,b=0,1
# for i in range(1,n+1):
#     print(a,end=" ")
#     a,b=b,a+b

# n=20
# for i in range(2,n+1):
#     prime=True
#     for j in range(2,i):
#         if i%j==0:
#             prime=False
#             break
#     if prime: 
#         print(i,end=" ")

# n=2
# if n<=1:
#     print("no prime")
# else:
#     for j in range(2,n):
#         if n%j==0:
#             print("not prime")
#             break
#     else: 
#         print(n,"prime")

# a=[111,33,10000]
# max=a[0]
# for i in a:
#     if i>max:
#         max=i
# print(max)
# max2=0
# for j in a:
#     if j>max2 and j!=max:
#         max2=j
# print(max2)


# a=["even" if i%2==0 else "odd" for i in range(1,11)]
# print(a)

# a=[[i for i in range(0,3)] for j in range(0,3)]
# print(a)

# a= [[0,1,2],[0,1,2]]
# b=[j for i in a for j in i]
# print(b)

# a=[22,333,1]
# b=print(sorted(a,key=lambda x:x[1]))
# b=print(sorted(a,key=lambda x:len(str(x))))
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(5))

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(0,9):
#     print(fib(i),end=" ")

# def nums(n):
#     if n==0:
#         return 0
#     else:
#         print(n)
#         nums(n-1)
        
# nums(5)

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+sum(n//10)
# print(sum(12345))


# def count(n):
#     if n==0:
#         return 0
#     else:
#         return 1+count(n//10)
# print(count(5)) 

# def rev(n):
#     if len(n)<=0:
#         return n
#     else:
#         return rev(n[1:])+n[0]
# print(rev("hima"))

# a="himavarsha"
# b={}
# for i in a:
#     if i in b:
#         b[i]=b[i]+1
#     else:
#         b[i]=1
# print(b)    
    # c=0
# for i in a:
#     print(a.count(i),i)


# a="himavarsha"
# b=""
# for i in a:
#     if a.count(i)==1:
#         b=b+i
#         break
# print(b)


# a=10
# b=200
# x,y=a,b
# while y!=0:
#     x,y=y,x%y
# gcd=x
# print(gcd)
# lcm=a*b/gcd
# print(lcm)


# def gcd(a,b):
#     if b==0:
#         return a
#     elif a==0:
#         return b
#     else:
#         return gcd(b,a%b)
# print(gcd(10,200))
# def lcm(a,b):
#     if b==0:
#         return a
#     elif a==0:
#         return b
#     else:
#         return a*b/gcd(a,b)
# print(lcm(10,20))


# for i in range(6,0,-1):
#     print(" "*(6-i)+"*"*i)

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(1,6):
#     print(" "*(6-i),end=" ")
#     print("* "*i)
# for j in range(6,0,-1):
#     print(" "*(6-j),end=" ")
#     print("* "*j)


# for i in range(1,7,2):
#     print(" "*(7-i),end=" ")
#     print("* "*i)
# for j in range(7,0,-2):
#     print(" "*(7-j),end=" ")
#     print("* "*j)


# a="hImaVrahsa"
# b=""
# for i in a:
#     if "A"<=i<="Z":
#         b=i+b
#     else:
#         b=b+i
# print(b)

# a=["A","B","C","D"]
# for i in range(len(a)):
#     for j in range(i+1):
#         print(a[j],end=" ")
#     print()

# a="abcdefghijklmnopqrstuvwxyz"
# k=0
# for i in range(1,5):
#     for j in range(i):
#         print(a[k],end=" ")
#         k=k+1
#     print()


# a=[1,2,2,3]
# repeat=[]
# for i in range(1,len(a)):
#     count=a.count(i)
#     if count>1:
#         repeat.append(i)
# print(repeat)


# a=[1,2,4]
# n=4
# for i in range(1,n+1):
#     if i not in a:
#         print(i)


# for i in range(1,6):
#     print(" "*(6-i),end=" ")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# for k in range(6,0,-1):
#     print(" "*(6-k),end=" ")
#     for l in range(1,k+1):
#         print(l,end=" ")
#     print()

# a="himavarsha"
# b=""
# for i in a:
#     if i not in b:
#         b=b+i
# print(b)

a=[22,11,33,2]
min=a[0]
for i in a:
    if i<min:
        min=i
print(min)
min2=max(a)
for j in a:
    if j<min2 and j!=min:
        min2=j
print(min2)