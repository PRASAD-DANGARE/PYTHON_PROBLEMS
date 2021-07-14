'''
Function Name    :  Array
Description      :  Accept Number From User & Display Even Number Using Array
Function Date    :  14 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

from array import *

#===============================
#
# Display Even Element Operation
#
#===============================

def Array(arr, iValue1):

    if arr == None or iValue1 <= 0:
        exit("Empty Input!")

    print("\nEven Elements Are : ")

    for i in range(0, iValue1):
        
        if arr[i] % 2 == 0:
            print(arr[i])

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

    if arr == None:
        exit("Unable To Allocate The Memory!")

    for _ in range(iNo1):
        arr.append(int(input("\nEnter The Elements : ")))

    print("\nTotal Index Of Array Are : ", len(arr))

    Array(arr, iNo1)


#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main() 
