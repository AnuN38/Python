class english():
    def greetings(self):
        print("Hello")
class french():
    def greetings(self):
        print("bonchu")
def intro(language):
    language.greetings()
e = english()
f = french()
e.greetings()
f.greetings()
