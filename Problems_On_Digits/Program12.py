'''
Function Name    :  Max_Digit
Description      :  Accept Number From User And Return Largest Digit, Reduce Time Complexcity V2
Function Date    :  09 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''
 
#============================
#
# Max_Digit Operation
#
#============================

def Max_Digit(iValue1):

    iDigit = 0
    iMax = 0

    if iValue1 < 0:
        iValue1 =- iValue1

    while iValue1 > 0:

        iDigit = iValue1 % 10
        
        if iDigit > iMax:
            iMax = iDigit

            if iMax == 9:
                break
        iValue1 = iValue1 // 10

    return iMax 

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    iRet = Max_Digit(iNo1)

    print("Largest Digit Is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
