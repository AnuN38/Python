"""Multi level inheritance"""

# class animal():
#     def eat(self):
#         print("eating")
# class dog(animal):
#     def bark(self):
#         print("barking")
# class puppy(dog):
#     def cry(self):
#         print("crying")
# p = puppy()
# p.bark()
# p.eat()
# p.cry()

"""Python multiple inheritance"""
# class apple():
#     def color(self):
#         print("Color is red")
# class banana():
#     def shape(self):
#         print("it is long")
# class fruits(apple,banana):
#     def fru(self):
#         print("apple and banana are fruits")
# fr = fruits()
# fr.shape()
# fr.color()
# fr.fru()


"""super()"""
class vehicle():
    def start(self):
        print("starting engine")
    def stop(self):
        print("stop engine")
class twowheeler(vehicle):
    def say(self):
        super().start()
        print("i have two wheels")
        super().stop()
pulser = twowheeler()
pulser.say()