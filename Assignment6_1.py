'''

Class Name    : Demo
Function Name : Fun(), Gun()
Description   : Two Instance Methods Of Class As Fun And Gun Which Displays Values Of Instance Variables 
Author        : Prasad Vijaykumar Dangare
Date          : 04 Mar 2021

'''

class Demo:

    Value = 100

    def __init__(self, i, j):
        self.no1 = i
        self.no2 = j

    def Fun(self):
        print("Inside Fun")
        print(self.no1, self.no2)

    def Gun(self):
        print("Inside Gun")
        print(self.no1, self.no2)

obj1 = Demo(11, 21)

obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()
