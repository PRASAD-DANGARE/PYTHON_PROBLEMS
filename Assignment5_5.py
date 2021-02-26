'''

Function Name : Recursion_Factorial()
Description   : Accept N Number From User And Find The Factorial Using Recursion 
Author        : Prasad Vijaykumar Dangare
Date          : 26 Feb 2021

'''

def Recursion_Factorial(iNo):

    if(iNo == 0):
        return 1
    return iNo * Recursion_Factorial(iNo - 1)

def main():

    value = int(input("Enter The Number : "))
    iRet = Recursion_Factorial(value)
    
    print("Factorial Of {} Is {} ".format(value, iRet)) 

if __name__ == "__main__":
    main()