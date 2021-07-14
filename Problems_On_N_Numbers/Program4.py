'''
Function Name    :  Array
Description      :  Accept Number From User & Display Addition Using Array
Function Date    :  14 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

from array import *

#===============================
#
# Add All Element Operation
#
#===============================

def Sum_Elements(arr, iValue1):

    iSum = 0

    for i in range(0, iValue1):
        iSum = iSum + arr[i]

    return iSum

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

    iRet = Sum_Elements(arr, iNo1)
    print("\nSummation Of All Elements Are : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main() 
