a="1020304050"
b=""
c=""
for i in a:
    if "1"<=i<="9":
        b=b+i
    elif i=="0":
        c=c+i
d=b+c
print(d)

str="python is a easy language python is powerful"
count={}
for i in str.split():
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

str="himavarsha"
b=""
for i in str:
    if i in "aeiou":
        b=b+i
print(b)
count={}
for j in b:
    if j in count:
        count[j]+=1
    else:
        count[j]=1
print(count)
max=0
for k in count:
    if count[k]>max:
        max=count[k]
        v=k
print(v)
