"""List"""

"""Access items"""

# b=["anu","anu","athira","athul"]
# print(b[3])

# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(a[2:4])

# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(a[-3])

# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(a[-6:-2])

"""Check if Item Exists"""

# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# if "orange" in a:
#     print("Yes,orange exist in the list")
# else:
#     print("Not exist")


"""Change list items"""

# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# a[3]="Hello"
# print(a)


# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# a[2:5]=["fruit1","fruit2"]
# print(a)

# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# a[1:2]=["red","green","yellow"]
# print(a)


"""insert items"""
# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# a.insert(3,"green")
# print(a)

"""Append items"""

# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# a.append("Red")
# print(a)

"""Extend list"""
# a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# colors=["Red","Green","Yellow","Blue"]
# a.extend(colors)
# print(a)


# a=["apple", "banana", "cherry", "orange", "kiwi"]
# b=("red","green","blue")
# a.extend(b)
# print(a)

# a=["apple", "banana", "cherry", "orange", "kiwi"]
# b={"red","green","blue"}
# a.extend(b)
# print(a)

"""Remove specified item"""
# a=["apple", "banana", "cherry", "orange", "kiwi"]
# a.remove("cherry")
# print(a)

"""Remove specified index"""
# a=["apple", "banana", "cherry", "orange", "kiwi"]
# a.pop(1)
# print(a)

# a=["apple", "banana", "cherry", "orange", "kiwi"]
# a.pop()
# print(a)

"""Remove specified index using del"""

# a=["apple", "banana", "cherry", "orange", "kiwi"]
# del a[0]
# print(a)

# a=["apple", "banana", "cherry", "orange", "kiwi"]
# del a
# print(a)

"""clear list"""

# a=["apple", "banana", "cherry", "orange", "kiwi"]
# a.clear()
# print(a)

"""Loop through a list"""

# a=["apple", "banana", "cherry", "orange"]
# for i in a:
#     print(i)


# a=["apple", "banana", "cherry"]
# for i in range(len(a)):
#     print(a[i])

"""print list using while"""
# a=["apple", "banana", "cherry", "orange", "kiwi"]
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+1


"""Sort list"""

# a = ["orange", "mango", "kiwi", "pineapple", "banana"]
# a.sort()
# print(a)


# b = [100, 200, 50, 150, 300]
# b.sort()
# print(b)

"""Descending order"""
# a = ["orange", "mango", "kiwi", "pineapple", "banana"]
# a.sort(reverse=True)
# print(a)


# b = [150, 300, 50, 100, 200]
# b.sort(reverse=True)
# print(b)

"""Case insensitive sort"""

# a = ["Orange", "mango", "kiwi", "Pineapple", "banana"]
# a.sort()
# print(a)


# a = ["orange", "mango", "kiwi", "pineapple", "banana"]
# a.sort(key=str.lower)
# print(a)


"""Reverse the list"""

# a = ["orange", "mango", "kiwi", "pineapple", "banana"]
# a.reverse()
# print(a)


"""Copy a list"""
# a = ["orange", "mango", "kiwi", "pineapple", "banana"]
# newlist = a.copy()
# print(newlist)

"""Copy list using list() method"""
# a = ["orange", "mango", "kiwi", "pineapple", "banana"]
# newlist = list(a)
# print(newlist)

"""Join two lists"""
# li1 = ["orange", "mango", "kiwi", "banana"]
# li2 = [90,70,50,30]
# li3 = li1 + li2
# print(li3)

"""Another way to join lists"""
# li1 = ["a", "n", "u"]
# li2 = [0, 3, 8, 9, 7]
# for i in li2:
#     li1.append(i)
# print(li1)

"""Join two lists using extend() method"""
# li1 = ["a", "n", "u"]
# li2 = [0, 3, 8, 9, 7]
# li1.extend(li2)
# print(li1)


"""Add items"""
# a = ["anu", "athira", "ashvi", "arjun"]
# a.append("ali")
# print(a)


"""Add item to a specified index"""
# a = ["anu", "athira", "ashvi", "arjun"]
# a.insert(1,"sam")
# print(a)


# a=["apple","orange","banana"]
# b=["red","green","orange"]
# a.extend(b)
# print(a)
# a.remove("orange")
# print(a)
# a.pop(2)
# print(a)

"""Tuple"""
# a = ("apple", "orange", "kiwi", "banana")
# print(type(a))
# print(len(a))

"""change tuple items"""
# a = ("apple", "orange", "banana")
# x = list(a)
# x[1]="kiwi"
# a=tuple(x)
# print(a)


# fruits = ("apple", "orange", "banana")
# (red,green,blue) = fruits
# print(red)
# print(green)
# print(blue)


"""Set"""
# s = {"apple","orange","kiwi","apple"}
# print(type(s))
# print(len(s))
# print(s)


"""Dictionary"""
# a={"name":"anu","place":"malappuram","year":2022}
# print(a)
# print(type(a))
# print(len(a))
# a["year"]=1999
# print(a)

# a={"name":"anu","place":"malappuram","year":2022}


# a=10
# b=10
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")


# a=["a","b","c","d"]
# for i in a:
#     print(a)


# fruits =["apple","banana","kiwi","orange","grape"]
# n = input("Enter a fruit name: ")
# for n in fruits:
#     print("Fruit exist")
#     break


fruits = ["apple", "banana", "kiwi", "orange", "grape"]
n = input("Enter a fruit name: ")
if n == "banana":
    print("Welcome")
else:
    print("Not entry")
