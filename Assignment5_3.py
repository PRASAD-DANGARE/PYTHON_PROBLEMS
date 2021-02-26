'''

Function Name : Recursion_Number_Printing()
Description   : Accept N Number From User And Print That Number In Reverse Order Using Recursion 
Author        : Prasad Vijaykumar Dangare
Date          : 26 Feb 2021

'''

def Recursion_Number_Printing(iNo):
    
    if (iNo > 0): 
        print(iNo, end = ' ') 
        Recursion_Number_Printing(iNo - 1) 
    
    '''if iNo > 0:
        print(iNo, end = " ")
        iNo = iNo - 1
        Recursion(iNo)
    '''

def main():

    value = int(input("Enter One Number : "))

    Recursion_Number_Printing(value)

if __name__ == "__main__":
    main()