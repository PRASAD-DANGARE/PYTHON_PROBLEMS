'''
Function Name    :  Frequency
Description      :  Accept Number From User And Find Frequency Of Given Digit By User
Function Date    :  09 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

#============================
#
# Frequency Operation
#
#============================

def Frequency(iValue1, iValue2):

    iCnt = 0
    iDigit = 0

    if iValue2 > 9:
        exit("Invalid Search! | Note : Give Input In Between 0 To 9")

    if iValue1 < 0:
        iValue1 =- iValue1

    while iValue1 > 0:

        iDigit = iValue1 % 10
        if iDigit == iValue2:
            iCnt += 1
        iValue1 = iValue1 // 10
    
    return iCnt

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))
    iNo2 = int(input("Enter The Digit To Search : "))

    iRet = Frequency(iNo1, iNo2)

    print("Frequency Of Searched Digit Is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
