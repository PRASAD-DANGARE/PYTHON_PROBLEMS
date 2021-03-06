'''
Function Name    :  Minimum
Description      :  Accept Number From User & Find Smallest Elements
Function Date    :  15 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

#===============================
#
# Minimum Number Operation
#
#===============================

from array import *

def Minimum(arr, iValue1):

    iMax = 0

    if arr == None:
        exit("Invalid Input!")

    iMax = arr[0]

    for i in range(0, iValue1):
        if arr[i] < iMax:
            iMax = arr[i]

    return iMax

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

    iRet = Minimum(arr, iNo1)
    print("\nSmallest Number is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
