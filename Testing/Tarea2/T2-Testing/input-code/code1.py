
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        return self.firstName + self.lastName

    def doit(self):
        eval("2+2")
        b = 8
        a = 2
        a = a + 3
        b = b + a
        c = a + b
        if a:
            a = 2
        else:
            pass
        
    def if_without_else(self):
        a = 1
        if a:
            a = 2
    
    def if_with_bad_else(self):
        a = 1
        if a:
            a = 2
        else:
            pass
        
    def if_with_else(self):
        a = 1
        if a:
            a = 2
        else:
            a = 3

    def somethig(self):
        if True:
            print("something")


