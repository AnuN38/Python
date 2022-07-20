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

'''OR'''

# a = [1,5,3,2]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         temp = 0
#         if a[i] > a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
# print(a)



"""Find the smallest and largest element in an array"""
# a = [10,5,3,2]
# l = len(a)
# for i in range(0,l):
#     for j in range(i+1,l):
#         temp = 0
#         if a[i] > a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
# print("smallest element:",a[0])
# print(a[l-1])


"""Find the minimum and maximum element in an array"""
# arr = [34,54,32,12,24,20]
# minV = min(arr)
# maxV = max(arr)
# print(minV)
# print(maxV)


"""Write a program to reverse the array"""
# a = [34,23,15,25,10,5]
# b = a[::-1]
# print(b)

'''OR'''

# a = [34,23,15,25,10,5]
# for i in range(len(a)-1,-1,-1):
#     print(a[i])


"""Create three arrays and find the common element in these arrays"""

# a = [10,15,20,25,30,35,45,50]
# b = [10,20,30,40,50,60,45]
# c = [10,13,15,17,20,45]
# for i in a:
#     for j in b:
#         for k in c:
#             if i==j and j==k:
#                 print(i)
#                 i = i+1
#                 j = j+1
#                 k = k+1






"""Sort the array 0s, 1s and 2s"""
# a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         temp = 0
#         if a[i] > a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
# print(a)




"""Spiral"""

# a = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16]]
#
# m = 4
# n = 4
# k = 0
# l = 0
# # Print the first row from
# # the remaining rows
# for i in range(l, n):
#     print(a[k][i], end=" ")
# k += 1
#
# # Print the last column from
# # the remaining columns
# for i in range(k, m):
#     print(a[i][n - 1], end=" ")
# n -= 1
#
# # Print the last row from
# # the remaining rows
# if (k < m):
#     for i in range(n - 1, (l - 1), -1):
#         print(a[m - 1][i], end=" ")
#     m -= 1
#
# # Print the first column from
# # the remaining columns
# if (l < n):
#     for i in range(m - 1, k - 1, -1):
#         print(a[i][l], end=" ")
#     l += 1


"""program to generate a dictionary that contains (i,i*i) such that is an integral number between 1 and n"""
a = {}
n = int(input("Enter a limit: "))
for i in range(1,n):
    a[i]=i*i
print(a)






