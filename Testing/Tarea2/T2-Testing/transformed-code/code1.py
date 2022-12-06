class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        return self.firstName + self.lastName

    def doit(self):
        literal_eval('2+2')
        b = 8
        a = 2
        a += 3
        b += a
        c = a + b
        if a:
            a = 2

    def somethig(self):
        print('something')