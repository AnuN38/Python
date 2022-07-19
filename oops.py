class person():
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def add(self):
        print("hello, my name is: " + self.name)


# object creation
p = person("anu", 24)
# print(p.name)
# print(p.age)
p.add()

# modify age
p.age=26
print(p.age)

# deleting values
del p.age
print(p.age)

