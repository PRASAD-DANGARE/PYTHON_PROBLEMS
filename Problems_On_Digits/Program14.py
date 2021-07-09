'''
Function Name    :  Min_Digit
Description      :  Accept Number From User And Return Smallest Digit
Function Date    :  09 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Min_Digit Operation
#
#============================


def Min_Digit(iValue1):

    iDigit = 0
    iMin = 9

    if iValue1 < 0:
        iValue1 =- iValue1

    while iValue1 > 0:

        iDigit = iValue1 % 10
        
        if iDigit < iMin:
            iMin = iDigit

            if iMin == 0:
                break

        iValue1 = iValue1 // 10

    return iMin

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    iRet = Min_Digit(iNo1)

    print("Minimum Number is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
