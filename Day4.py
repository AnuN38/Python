# name=arun,athul,amal
# passward=a123,b123,c123

# a=["Arun","Athul","Amal"]
# pwd=["a123","b123","c123"]
# n=input("Enter your name:")
# for i in a:
#     p=input("Enter your password")
#     for i in pwd:
#         if (a[0]==n and pwd[0]==p) or (a[1]==n and pwd[1]==p) or (a[2]==n and pwd[2]==p):
#             print("Logged In")
#             break
#     else:
#         print("Password is incorrect")




a=["Arun","Athul","Amal"]
b=["a123","b123","c123"]
n=input("Enter your name:")
if n in a:
    pwd=input("Enter your password:")
    ind=a.index(n)
    if pwd in b and ind==b.index(pwd):
        print("Logged In")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")

