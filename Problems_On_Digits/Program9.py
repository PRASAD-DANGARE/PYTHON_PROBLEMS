'''
Function Name    :  Reverse
Description      :  Accept Number From User And Return Reverse Of That Number Using For-Loop
Function Date    :  09 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Reverse Operation
#
#============================

def Reverse(iValue1):

    iDigit = 0
    iRev = 0

    if iValue1 < 0:
        exit("Invalid Input! | Note : Give Input Greater Than 0")

    for _ in range(iValue1):

        if iValue1 == 0:
            break

        iDigit = iValue1 % 10
        iRev = (iRev * 10) + iDigit
        iValue1 = iValue1 // 10

    return iRev

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    iRet = Reverse(iNo1)

    print("Reverse Number is : ", iRet)

#====================
#
# Code Starter
#
#====================


if __name__ == "__main__":
    main()
