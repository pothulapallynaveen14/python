# ==========================
# Type Conversion in Python
# ==========================

print("Type Conversion Examples 🚀")


# --------------------------
# String to Integer
# --------------------------

num = "100"

converted_num = int(num)

print("\nString to Integer:")
print(converted_num)
print(type(converted_num))


# --------------------------
# Integer to Float
# --------------------------

number = 25

value = float(number)

print("\nInteger to Float:")
print(value)
print(type(value))


# --------------------------
# Number to String
# --------------------------

age = 22

text = str(age)

print("\nNumber to String:")
print(text)
print(type(text))


# --------------------------
# Boolean Conversion
# --------------------------

print("\nBoolean Conversion:")

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1,2]))


# --------------------------
# Input Problem Example
# --------------------------

print("\nWithout Conversion:")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("Result:", num1 + num2)


# --------------------------
# Correct Way
# --------------------------

print("\nWith Integer Conversion:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)


# --------------------------
# Mini Task
# --------------------------

print("\nStudent Information")

name = input("Enter name: ")
age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))

print("\nStudent Details")
print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)


print("\nTopic Completed ✅")
