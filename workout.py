"""Factorial of a number using array"""
# def factArray(a):
#     for i in a:
#         fact = 1
#         for j in range(1,i+1):
#             fact = fact * j
#         print(fact)
# b = [2,4,5,6,1,0]
# factArray(b)


"""Given a random set of numbers, print them in sorted order"""
# a = [1,5,3,2]
# a.sort()
# print(a)

# a = [1,5,3,2]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         temp = 0
#         if a[i] > a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
# print(a)



'''Find the smallest and largest element in an array'''
a = [1,5,3,2]
l = len(a)
for i in range(0,l):
    for j in range(i+1,l):
        temp = 0
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a[0])
print(a[l-1])


















