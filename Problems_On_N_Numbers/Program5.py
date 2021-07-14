'''
Function Name    :  Array
Description      :  Accept Number From User & Display Addition Of Even Numbers Using Array
Function Date    :  14 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

from array import *

#===============================
#
# Add Even Element Operation
#
#===============================

def Sum_Even_Elements(arr, iValue1):

    iSum = 0

    print("\nEven Elements Are : ")
    for i in range(0, iValue1):

        if arr[i] % 2 == 0:
            iSum = iSum + arr[i]
            print(arr[i])

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

    iRet = Sum_Even_Elements(arr, iNo1)
    print("\nSummation Of All Even Elements Are : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main() 
