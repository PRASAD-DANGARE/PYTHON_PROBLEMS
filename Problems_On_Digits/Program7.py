'''
Function Name    :  Mult_Digits
Description      :  Accept Number From User And Multiplication All The Numbers Except 0
Function Date    :  05 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Mult_Digits Operation
#
#============================

def Mult_Digits(iValue1):
    
    iDigit = 0
    iMult = 1

    if iValue1 < 0:
        iValue1 =- iValue1

    while iValue1 > 0:

        iDigit = iValue1 % 10
        if iDigit != 0:
            iMult = iMult * iDigit
        iValue1 = iValue1 // 10

    return iMult

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    iRet = Mult_Digits(iNo1)

    print("Multiplication Of {0} Digits is {1} ".format(iNo1, iRet))

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
