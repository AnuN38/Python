# filename = "1.txt"
# file = open(filename,"r")
# # for line in file:
# #     print(line)
#
# # print(file.read())
# # print(file.read(5))
#
# # print(file.readline())
# print(file.readlines())
# file.close()


"""Writing into a file"""

# file = open("1.txt","w")
# file.write("aand ksknsf jfskmennf")
# file.close()
# file = open("1.txt","r")
# print(file.readlines())
# file.close()
# file = open("1.txt","a")
# file.write(" ass kdsnbcb sjfbmb end")
# file.close()
# file = open("1.txt","r")
# print(file.read())


"""Creating a new file"""
# f = open("abc.txt","x")
# f.close()

"""Remove file"""
# import os
# os.remove("abc.txt")

"""Error handling"""
import os
# if os.path.exists("abc.txt"):
#     os.remove("abc.txt")
# else:
#     print("File not exist")

"""Remove a directory"""
# os.rmdir("new")

"""Get current directory"""
# os.getcwd()

"""change directory"""
# os.chdir("C:\Users\anuna\Desktop\Python\Notes")
# print("1",os.getcwd())
#
# print(os.listdir())

"""Making new directory"""
# os.mkdir("demodir")
# print(os.listdir())


