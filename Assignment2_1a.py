'''

Function Name : main()
Description   : Calling The Module From Assignment2_1b.py 
Author        : Prasad Vijaykumar Dangare
Date          : 18-02-2021 

'''


import Assignment2_1b as MyModule # Importing Module Which Contain Function In It

def main():
    value1 = int(input("\nEnter First Number : "))
    value2 = int(input("Enter Second Number : "))
    print("\n")

    Addition = MyModule.Add(value1, value2) # Calling the Function Of Module As MyModule
    print("Addition Of {} And {} Is {} ".format(value1, value2, Addition))
    print("\n")

    Subtraction = MyModule.Sub(value1, value2)
    print("Subtraction Of {} And {} Is {} ".format(value1, value2, Subtraction))
    print("\n")

    Multiplication = MyModule.Mult(value1, value2)
    print("Multiplication Of {} And {} Is {} ".format(value1, value2, Multiplication))
    print("\n")

    Division = MyModule.Div(value1, value2)
    print("Division Of {} And {} Is {} ".format(value1, value2, Division))
    print("\n")

if __name__ == "__main__":
    main()