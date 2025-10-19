# ----------------------------------------------------------
# 📘 Assignment: Strings Built-In Functions
# Tech Stack: Python
# ----------------------------------------------------------

# 1️⃣ Strings Built-In Functions
print("------ Strings Built-In Functions ------")

text = "Python Programming"

print("Length of string:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("String repeated twice:", text * 2)
print("String sliced (0 to 6):", text[0:6])
print("Check if 'Python' in text:", "Python" in text)
print("Check if 'Java' not in text:", "Java" not in text)

# ----------------------------------------------------------
# 2️⃣ Case Conversion Built-In Functions
print("\n------ Case Conversion Built-In Functions ------")

sample = "hElLo WoRlD"
print("Original:", sample)
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Title case:", sample.title())
print("Capitalize:", sample.capitalize())
print("Swapcase:", sample.swapcase())

# ----------------------------------------------------------
# 3️⃣ Trimming and Replace Built-In Functions
print("\n------ Trimming and Replace Built-In Functions ------")

data = "   Python is fun!   "
print("Original:", repr(data))
print("After strip():", repr(data.strip()))
print("After lstrip():", repr(data.lstrip()))
print("After rstrip():", repr(data.rstrip()))
print("Replace 'fun' with 'powerful':", data.replace("fun", "powerful"))

# ----------------------------------------------------------
# 4️⃣ Searching and Finding Built-In Functions
print("\n------ Searching and Finding Built-In Functions ------")

sentence = "Learning Python is easy and enjoyable"
print("Find position of 'Python':", sentence.find("Python"))
print("Index of 'easy':", sentence.index("easy"))
print("Count of 'a':", sentence.count("a"))
print("Starts with 'Learning':", sentence.startswith("Learning"))
print("Ends with 'enjoyable':", sentence.endswith("enjoyable"))

# ----------------------------------------------------------
# ✅ End of Assignment
# ----------------------------------------------------------
