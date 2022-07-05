# for i in range(1,6):
#     print("*")


# Pattern printing
# n=int(input("Enter the number of rows:"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=' ')
#     print("\n")


# Number pyramid
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print("\n")


# st=65
# li=int(input("Enter the limit:"))
# for i in range(0,li):
#     for j in range(0,i+1):
#          print(chr(st),end='')
#          st=st+1
#     print("\n")



# n= int(input("Enter the limit:"))
# for i in range(0,n):
#     start=65
#     for j in range(0,i+1):
#         print(chr(start),end='')
#         start=start+1
#     print()


# n=int(input("Enter the number of rows:"))
# k=n-1
# for i in range(0,n):
#     for j in range(0,k):
#         print(end=' ')
#     k=k-1
#     for j in range(0,i+1):
#         print("*",end=' ')
#     print()


# for i in range(6):
#     for j in range(7):
#         if (i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()


# for i in range(4):
#     for j in range(7):
#         if (i+j==3) or (i-j==-3) or (i==2 and j==2) or (i==2 and j==3) or (i==2 and j==4):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()


# for i in range(5):
#     for j in range(5):
#         if (i%6!=0 and (j==0) or (j==4)) or ((i==0) or (i==2) and (j==1 or 2 or 3)):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()


n=int(input("Enter the number of rows:"))
for i in range(n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
