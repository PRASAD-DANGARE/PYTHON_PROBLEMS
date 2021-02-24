'''

Function Name : main()
Description   : Accept N Numbers From User And Multiply The Number Using Lambda Function 
Author        : Prasad Vijaykumar Dangare
Date          : 24 Feb 2021

'''   

def main():

    Mult = lambda iNo1, iNo2 : iNo1 * iNo2

    value1 = int(input("Enter First Number For Multiply : "))

    value2 = int(input("Enter Second Number For Multiply : "))

    ret = Mult(value1, value2)
    print("Multiplication Of {} And {} Is {} ".format(value1, value2, ret))

if __name__ == "__main__":
    main()