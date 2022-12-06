class Person:

    def fullName(self):
        return self.firstName + self.lastName

    def unused(self):
        a = 0
        return 1

class Person2:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

def example():
    x = 2
    y = 3
    z = 4
    return y + z