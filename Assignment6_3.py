'''

Class Name    : Arithmatic
Function Name : Addition(), Subtraction(), Multiplication(), Division()
Description   : Accept N Number From User & Perform Addition, Subtraction, Multiplication, Division Using OOP 
Author        : Prasad Vijaykumar Dangare
Date          : 04 Mar 2021

'''

class Arithmatic:
    
    def __init__(self, iValue1, iValue2):
        self.iValue1 = iValue1
        self.iValue2 = iValue2

    def Addition(self):
        return self.iValue1 + self.iValue2

    def Subtraction(self):
        return self.iValue1 - self.iValue2

    def Multiplication(self):
        return self.iValue1 * self.iValue2

    def Division(self):
        return self.iValue1 / self.iValue2

def main():

    iValue1 = int(input("Enter First Number : "))
    iValue2 = int(input("Enter Second Number : "))

    
    obj1 = Arithmatic(iValue1, iValue2)
    print("Addition is : ", obj1.Addition())

    obj2 = Arithmatic(iValue1, iValue2)
    print("Subtraction is : ", obj2.Subtraction())

    obj3 = Arithmatic(iValue1, iValue2)
    print("Multiplication is : ", obj3.Multiplication())

    obj4 = Arithmatic(iValue1, iValue2)
    print("Division is : ", obj4.Division())

if __name__ == "__main__":
    main()