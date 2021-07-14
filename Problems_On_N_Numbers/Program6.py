'''
Function Name    :  Even_Count
Description      :  Accept Number From User & Display Count Of Even Numbers Using Array
Function Date    :  14 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

from array import *

#===============================
#
# Count Even Element Operation
#
#===============================

def Even_Count(arr, iValue1):
    
    iCnt = 0

    for i in range(0, iValue1):

        if arr[i] % 2 == 0:
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

    print("\nTotal Index Of Array Are : ", len(arr))

    iRet = Even_Count(arr, iNo1)
    print("\nCount Of All Even Elements Are : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
