# Largest of three numbers

# a=int(input("Enter first number:"))
# b=int(input("Enter sec number:"))
# c=int(input("Enter third number:"))
# if a > b:
#     if a > c:
#         print("a is the largest number")
#     else:
#         print("c is the largest number")
# else:
#     if b > c:
#         print("b is the largest number")
#     else:
#         print("c is the largest number")


# a=int(input("Enter first number:"))
# b=int(input("Enter sec number:"))
# c=int(input("Enter third number:"))
# if a > b and a > c:
#     print("a is the largest number")
# elif b > c:
#     print("b is the largest number")
# else:
#     print("c is the largest number")


# Calculator

a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
c = input("Enter the operation:")
if c == "+":
    d = a + b
    print(d)
elif c == "-":
    d = a - b
    print(d)
elif c == "*":
    d = a * b
    print(d)
elif c == "/":
    d = a / b
    print(d)
elif c == "%":
    d = a % b
    print(d)
elif c == "//":
    d = a // b
    print(d)
else:
    print("Error")
