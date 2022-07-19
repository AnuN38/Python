class person():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)
# p = person("anu","nallatt")
# p.printname()
class child(person):
    def printage(self,age):
        self.age=age
        print(self.age)

    # def __init__(self,fname,lname):
    #     person.__init__(self,fname,lname)
    #
    # def printage(self,age):
    #     self.age = age
    #     print(self.age)
c = child("sam","ram")
c.printname()
c.printage(22)
# c.printage(34)
