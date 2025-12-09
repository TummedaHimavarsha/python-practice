data=open("./tecxt.txt","r")
ip=data.read()
print(ip)
data.close()

data2=open("./tecxt.txt","r")
ip=data2.readline()
print(ip)

data3=open("tecxt.txt","r")
ip3=data3.readlines()
print(ip3)

a=open("./tecxt.txt","w")
a.write("hi hello")
a.close()


a=open("tecxt.txt","w")
a.write("Namaste python")
a.close()

ab=open("tecxt.txt","a")
ab.writelines(["a\n","b\n"])

ab=open("tecxt.txt","a")
ab.writelines(["k","l"])
print(ab.closed)
ab.close()
print(ab.closed)

try:
    a=open("dfas.txt","r")
except FileNotFoundError:
    print("no such file")

with open("tecxt.txt","r") as f:
    print(f.read())

with open("tecxt.txt","r") as f:
    print(f.readline())

with open("tecxt.txt","r") as f:
    print(f.readlines())

with open("tecxt.txt","w") as f:
    print(f.write("something"))

with open("tecxt.txt","w") as f:
    print(f.writelines(["sum\n","else\n"]))

with open("tecxt.txt","a") as f:
    print(f.write("more"))

s
ab=open("tecxt.txt","w")
ab.write("hi")
print(ab)
print(ab.closed)
ab.close()
print(ab.closed)

# • What is file handling?
filehandling is used to perform operations like creating,updating,
removing,deleting,reading,writing

# • read() vs readline() vs readlines()?
read():is used to read the entore file at a time
readline():is used to read the file line by line 
readlines():return the file in list

# • Why use with open()?
to open the file

# • Difference between w and a
w mode: overwrites and the pointer is at start
a mode: wont overwrite just append the new data , and the pointer starts from the end

# • What is file pointer?
It tells the program where it is currently working inside the file
