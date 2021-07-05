'''
Function Name    :  Sum_Digits
Description      :  Accept Digit From User And Return Addition Of All Digits Of That Number V2
Function Date    :  05 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Sum_Digits Operation
#
#============================

def Sum_Digits(iValue1):

    iSum = 0

    while iValue1 > 0:
        iSum = iSum + (iValue1 % 10)
        iValue1 = iValue1 // 10

    return iSum

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter First Number : "))

    iRet = Sum_Digits(iNo1)

    print("Sum Of All Digits {0} Is : {1}".format(iNo1, iRet))

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
