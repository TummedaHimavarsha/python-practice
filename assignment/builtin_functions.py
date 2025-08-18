#document for built-in functions
#case conversion built-in functions
#1.upper()
a='hima'
b=a.upper()
print(f'upper case of the given string is {b}')
#2.lower()
c=a.lower()
print(f'lower case of the given string is {c}')
#3.title()
z='hima varsha'
d=z.title()
print(f'title case of the given string is {d}')
#4.capitalize()
e=z.capitalize() #only index[0] is capitalized
print(f'capitalize case of the given string is {e}')
#5.swapcase()
y='HIma VaRsHa'
f=y.swapcase() #capital into small and small into capital
print(f'the swapcase of the given string is {f}')
#6.is lower()
g=a.islower()#if the given string is in lower case it will print a bool value 
print(f'the given case is in lower : {g}')
#7 .upper()
h=a.isupper()
print(f'the given case is in lower : {h}')

#Trimming and replace Built-in Functions
#These functions help in removing or replacing characters.
#1.strip() ----- removes the white space from both ends
A="     Hima Varsha       "
print(A.strip())
#2.lstrip() -------- removes the left side white space
print(A.lstrip())
#3. rstrip() ===== remove the right side white space
print(A.rstrip())
#4.replace() ------- Replaces a substring with another substring.
B=" i am a  java developer "
print(B.replace("java","python"))


#3.Searching and Finding Built-in Functions
# These functions help in locating substrings inside strings.

  #1.find(substring) ------> Returns the first index of substring, or -1 if not found.
C='hima varsha'
print(C.find("a"))
print(C.find('z'))
print(C.find('hima varsha'))

#2. rfind(substring) =----> Returns the last index of substring, or -1.
print(C.rfind('a'))

#3.index(substring) → Same as find() but raises an error if not found.


#4.rindex(substring) → Same as rfind() but raises an error if not found.
print(C.rindex("a"))

# 5.count(substring) → Returns the number of occurrences of substring.
text='banana'
word=text.count("a")
print(f'the count of letter a in {text} is : {word} times')



