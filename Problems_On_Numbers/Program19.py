'''
Function Name    :  Factors
Description      :  Accept Number From User And Find Factors In Reverse / Discending Order
Function Date    :  09 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

#============================
#
# Factors Operation
#
#============================

def Factors(iValue1):

    if iValue1 < 0:
        exit("Invalid Input! | Note : Give Input Greater Than 0")

    for iCnt in range(iValue1 - 1, 0, -1):
        if iValue1 % iCnt == 0:
            print(iCnt)

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    Factors(iNo1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
