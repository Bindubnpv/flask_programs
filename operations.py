from exception1 import *
class Operator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def divi(self):
        return self.a / self.b

#a = int(input('enter first number:'))
#b = int(input('enter second number:'))
'''
for checking purpose i wrote 
a1 = Operator(a,b)
print(a1.add())
print(a1.sub())
print(a1.mul())
print(a1.divi())
'''


        