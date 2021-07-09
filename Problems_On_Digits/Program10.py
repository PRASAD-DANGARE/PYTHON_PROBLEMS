'''
Function Name    :  Check_Palindrome
Description      :  Accept Number From User And Check Whether That Number Is Pallindrone Or Not
Function Date    :  09 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Check_Palindrome Operation
#
#============================

def Check_Palindrome(iValue1):

    iDigit = 0
    iRev = 0
    iTemp = 0

    if iValue1 < 0:
        iValue1 =- iValue1

    iTemp = iValue1

    while iValue1 > 0:

        iDigit = iValue1 % 10
        iRev = (iRev * 10) + iDigit
        iValue1 = iValue1 // 10

    if iRev == iTemp:
        return True

    else:
        return False

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    bRet = Check_Palindrome(iNo1)

    if bRet == True:
        print(iNo1, "Is A Palindrome Number")

    else:
        print(iNo1, "Is Not A Palindrome Number")


#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
