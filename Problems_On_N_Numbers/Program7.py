'''
Function Name    :  Frequency
Description      :  Accept Number From User & Search An Element & Find The Frequency Using Array
Function Date    :  14 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int, Int
Output           :  Int

'''

from array import *

#===============================
#
# Count Frequency Operation
#
#===============================

def Frequency(arr, iValue1, iValue2):

    iCnt = 0

    for i in range(0, iValue1):

        if arr[i] == iValue2:
            iCnt += 1

    return iCnt

#====================
#
# Entry Point 
#
#====================

def main():

    arr = array('i', [])

    iNo1 = int(input("\nEnter Number Of Elements : "))

    if iNo1 <= 0:
        exit("Invalid Input! | Note : Give Input Greater Than 0")
    
    for _ in range(iNo1):
        arr.append(int(input("\nEnter The Elements : ")))

    iNo2 = int(input("\nEnter The Elements That You Want To Search : "))

    if iNo2 <= 0:
        exit("Invalid Input! | Note : Give Input Greater Than 0")

    iRet = Frequency(arr, iNo1, iNo2)
    print("\nFrequency Of Searched Element Is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
