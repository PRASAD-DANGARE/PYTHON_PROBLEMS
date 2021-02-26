'''

Function Name : Recursion_Number_Printing()
Description   : Accept N Number From User And Print That Number Using Recursion 
Author        : Prasad Vijaykumar Dangare
Date          : 26 Feb 2021

'''

def Recursion_Number_Printing(iNo): 

    if (iNo > 0): 
        Recursion_Number_Printing(iNo - 1) 
        print(iNo, end = ' ') 
        
def main():

    value = int(input("Enter One Number : "))

    Recursion_Number_Printing(value)

if __name__ == "__main__":
    main() 