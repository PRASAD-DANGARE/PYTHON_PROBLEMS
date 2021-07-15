'''
Function Name    :  Last_Occurance
Description      :  Accept Number From User & Find The Last Occurance Of The Element
Function Date    :  15 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int, Int
Output           :  Int

'''

#===============================
#
# Last Occurance Operation
#
#===============================

from array import *

def Last_Occurance(arr, iValue1, iValue2):

    iPos = 0

    for i in range(iValue1 - 1, -1, -1):

        if arr[i] == iValue2:
            iPos = i
            break

    if iPos == 0:
        return -1
    
    else:
        return i

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

    iRet = Last_Occurance(arr, iNo1, iNo2)

    if iRet == -1:
        print("Number Not Found!")
    else:
        print("Last Occurance Is At : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
