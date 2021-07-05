'''
Function Name    :  Even_Digits
Description      :  Accept Digit From User And Find How Many Numbers Are Even In That Digit V2
Function Date    :  05 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Even_Digits Operation
#
#============================

def Even_Digits(iValue1):

    iDigit = 0
    iCnt = 0

    if iValue1 < 0:
        iValue1 =- iValue1

    if iValue1 <= 0:
        exit("Invalid Input!")

    while iValue1 > 0:

        if (((iValue1 % 10) % 2) == 0):
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

    iRet = Even_Digits(iNo1)

    print("Number Of Even Digits From {0} Is : {1}".format(iNo1, iRet))

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
