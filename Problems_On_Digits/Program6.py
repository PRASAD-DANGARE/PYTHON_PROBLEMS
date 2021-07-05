'''
Function Name    :  Digit_Frequency
Description      :  Accept Digit From User And Find The Frequency Of That Digit(check how many times number occures in the digit)
Function Date    :  05 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

#============================
#
# Digit_Frequency Operation
#
#============================

def Digit_Frequency(iValue1, iValue2):

    iDigit = 0
    iCnt = 0

    if iValue1 < 0:
        iValue1 =- iValue1

    if iValue2 < 0 or iValue2 > 9:
        exit("Inavlid Digits! | Note : Digits Is In Between 0 To 9")

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
    iNo2 = int(input("Enter The Digit To Count Frequency : "))

    iRet = Digit_Frequency(iNo1, iNo2)

    print("Frequency Of Given Digits From {0} Is : {1}".format(iNo1, iRet))
    
#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
