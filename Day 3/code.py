# ==========================
# Day 3 - Conditional Statements
# if | if else | elif | nested if
# ==========================

print("Day 3 Started 🚀")


# --------------------------
# if Statement
# --------------------------

print("\nif Statement Example")

age = 20

if age >= 18:
    print("Eligible to vote")


# --------------------------
# if else Statement
# --------------------------

print("\nif else Example")

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# --------------------------
# elif Statement
# --------------------------

print("\nelif Example")

marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")


# --------------------------
# Nested if Statement
# --------------------------

print("\nNested if Example")

age = 22

if age >= 18:

    if age >= 21:
        print("Eligible for higher responsibilities")


# --------------------------
# Login System
# --------------------------

print("\nLogin System")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":

    if password == "1234":
        print("Login Successful")

    else:
        print("Wrong Password")

else:
    print("Invalid Username")


# --------------------------
# Largest of Two Numbers
# --------------------------

print("\nLargest Number")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")

else:
    print(b, "is greater")


# --------------------------
# Grade Calculator
# --------------------------

print("\nGrade Calculator")

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")


print("\nDay 3 Completed ✅")
