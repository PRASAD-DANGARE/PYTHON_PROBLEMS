'''
Function Name    :  Max_Min
Description      :  Accept Digit From User And Find Maximum & Minimum Digit & Find Difference V2
Function Date    :  10 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Max_Min Operation
#
#============================

def Max_Min(iValue1):

    iMax = 0
    iMin = 9

    Max = iValue1

    if iValue1 <= 0:
        exit("Invalid Input! | Note : Give Input Greater Than 0")

    for iDigit in range(1, Max):
        iDigit = Max % 10
        if iDigit > iMax:
            iMax = iDigit
        Max = Max // 10

    print("Maximum Number is : ", iMax)

    while iValue1 > 0:

        iDigit = iValue1 % 10
        if iDigit < iMin:
            iMin = iDigit
        iValue1 = iValue1 // 10

    print("Minimum Number is : ", iMin)

    return iMax - iMin

#====================
#
# Entry Point 
#
#====================
    
def main():

    iNo1 = int(input("Enter The Number : "))
    iRet = Max_Min(iNo1)

    print("Difference is : ", iRet)

#====================
#
# Code Starter
#
#====================


if __name__ == "__main__":
    main()
