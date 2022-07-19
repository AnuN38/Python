"""Tuple"""

# mytuple = ("apple","banana","orange","cherry")
# print(mytuple)

"""Tuple constructor"""

# a = tuple(("apple", "banana", "cherry"))
# print(a)
# print(type(a))


"""Access tuple items"""

# a = tuple(("apple", "banana", "cherry"))
# print(a[2])


# a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(a[2:4])

# a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# if "orange" in a:
#     print("Yes")


"""Change tuple values"""

# x = ("apple", "orange", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

"""Add items"""
"""1. convert to list"""
# x = ("apple", "orange", "cherry")
# y = list(x)
# y.append("banana")
# x = tuple(y)
# print(x)

"""2. Add tuple to a tuple"""
# x = ("apple", "orange", "cherry")
# y = ("banana",)
# x = x + y
# print(x)


"""Remove items"""

# x = ("apple", "banana", "cherry")
# y = list(x)
# y.remove("apple")
# x = tuple(y)
# print(x)

# x = ("apple", "banana", "cherry")
# del x
# print(x)


"""Unpacking a tuple"""

# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

"""Using asterisk"""
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, *yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

"""Loop through a tuple"""

# x=("apple","banana","orange","kiwi")
# for i in x:
#     print(i)

"""Loop through the index numbers"""

# x=("apple","banana","orange","kiwi")
# for i in range(len(x)):
#     print(x[i])

"""Using while loop"""

# x = ("apple", "banana", "orange", "kiwi")
# i = 0
# while i < (len(x)):
#     print(x[i])
#     i = i + 1


"""Join two tuples"""

# x = ("apple", "banana", "orange", "kiwi")
# y = ("red", "green", "blue")
# z = x + y
# print(z)

"""Multiply tuples"""

x = ("apple", "banana", "orange")
newTuple = x * 2
print(newTuple)


