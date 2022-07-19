class grandfather():
    def behaviour(self):
        name_gf="x"
        value = 100
        print("I have one grand child")

class father(grandfather):
    def a(self):
        name_fa ="abc"
        print("I am abc")

class mother():
    def b(self):
        name_mo="susu"
        value = 10
        son = 2
        print("I have long hair")

class son1(father,mother):
    def c(self):
        print("I am one son")

class son2(father,mother):
    def d(self):
        print("I am son2")

class daughter(father,mother):
    def e(self):
        print("I am daughter")

class grandchild(son2):
    def gs(self):
        print("I am the grand child")

obj =grandchild()
obj.a()
obj.behaviour()