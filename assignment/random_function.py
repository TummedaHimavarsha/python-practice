import random
list=[]
for i in range(5): 
    var=random.randint(10,50) 
    list.append(var) 
print(list)
print(random.random())
print(random.randint(1,101))
list2=["porsche","bmw","aston martin","fortuner","buggati"]
print(random.choice(list2))
list3=[1,2,3,4,5]
print(random.sample(list3,k=2))


