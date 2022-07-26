# class student():
#     def __init__(self):
#         print("This is a non parameterized constructor")
#     def show(self,name):
#         print("Hello",name)
# s = student()
# s.show("anu")

class student():
    def __init__(self,name):
        print("This is a parameterized constructor")
        self.name = name
    def show(self):
        print("Hello",self.name)
s = student("sam")
s.show()
