'''
Function Name    :  Array
Description      :  Accept Number From User & Display That Number Using Array V2
Function Date    :  14 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

from array import *

#============================
#
# Array Display Operation
#
#============================

def Array(arr, iValue1):

    print("\nElements From The Array Are : ")

    for i in range(0, iValue1):
        print(arr[i])

#====================
#
# Entry Point 
#
#====================

def main():

    arr = array('i', [])
    print(type(arr))

    iNo1 = int(input("\nEnter Number Of Elements : "))

    if iNo1 <= 0:
        exit("Invalid Input! | Note : Give Input Greater Than 0")

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
