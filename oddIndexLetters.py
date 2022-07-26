"""1. read a string and print odd index letters"""

# str = input("Enter a string: ")
# i=1
# while i < len(str):
#     print(str[i])
#     i = i + 2


"""2. Calculate the sum of all numbers from 1 to the given number"""

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)


"""3. Display fibonacci numbers"""

# n = int(input("Enter a number: "))
# n1 = 0
# n2 = 1
# for i in range(1,n+1):
#     print(n1)
#     sum = n1 + n2
#     n1 = n2
#     n2 = sum


"""4. Factorial of a number"""

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)
