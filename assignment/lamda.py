sqr=lambda x:x*x
print(sqr(6))

ab=lambda a:"even" if a%2==0 else "odd"
print(ab(9))

ma=lambda a,b:a if a>b else b
print(ma(10,20))

tw=lambda x,y:x+y
print(tw(2,30)) 


data = [(1, 5), (2, 3), (4, 1)]
result = sorted(data, key=lambda x: x[1])
print(result)


a=[1,2,3,4,5,6,7,8,9,10]
b=print(list(filter(lambda x:x%2==0,a))) 

a=[1,2,3,4,5]
b=print(list(map(lambda x:x**3,a)))

a=[2, 3, 4,5]
b=print(list(map(lambda x:x*x,a)))

b=lambda x: "positive" if x>0 else("zero" if x==0 else "negative")
print(b(0))

from functools import reduce
result = reduce(lambda x, y: x * y, [2, 3, 4, 5])
print(result)


a=["apple", "banana", "kiwi", "grapes"] 
result=sorted(a,key=lambda x:len(x))
print(result)

a=["Cat", "apple", "Banana", "dog"]
result=sorted(a,key=lambda x:len(x))
print(result)

a=["madam", "python", "level", "world"]
result=list(filter(lambda x:x==x[::-1],a))
print(result)



