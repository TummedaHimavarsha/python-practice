"""def cube(n):
    return n*n*n
vr=cube(2)
print(vr)""" #cube
"""def avg(a,b):
    return a+b/29
print(avg(2,4))"""# avg
"""def sum(n):
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum
print(sum(1235)) #sum of numbers
"""
"""def greet(name="guest"):
    print(f'welcome {name}')
greet()""" #default parameters
"""def greet(name='guest'):
    return "Hello,f' {name}"
print(greet("alice"))"""
"""n=5
def mul():
    global n
    for i in range(1,11):
        a=n*i
        print(a)
mul() """ # global variable example
"""def largest_div7():
    max_num = 0
    for i in range(1, 51):
        if i % 7 == 0:
            max_num = i
    return max_num
print(largest_div7())"""
"""def dict(*num):
    for i in num:
        print(i)
dict({'name': 'hima', 'age': 23, 'address': 'kphb'}) """
"""def string(**ar):
    for i,j in ar.items():
        print(f'{i}:{j}')
string(name='hima', age=23, address='kphb') """
 # This line is corrected to match the function definition
"""def add(a,b):
    return a+b,a-b,a*b
add,sub,mul=add(2,3)
print(f'addition is {add},subtraction is {sub},multiplication is {mul}') """ # This line is corrected to match the function definition