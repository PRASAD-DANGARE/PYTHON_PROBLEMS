'''
Function Name    :  Frequency
Description      :  Accept Number From User & Search An Element And Find The First Index Of That Number Using Array
Function Date    :  14 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int, Int
Output           :  Int

'''

from array import *

#===============================
#
# First Occurance Operation
#
#===============================

def Frequency(arr, iValue1, iValue2):

    First_Occ = -1
    
    for i in range(0, iValue1):

        if arr[i] == iValue2:
            First_Occ = i
            break

    if First_Occ != -1:
        return i
        #print("First Occurance Is At : ", First_Occ)
    else:
        return -1
        #print("Number Not Found!")

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

    if iRet == -1:
        print("Number Not Found!")
    else:
        print("First Occurance Is At : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
