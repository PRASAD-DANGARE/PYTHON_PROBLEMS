'''
Function Name    :  main
Description      :  Accept Number From User & Display That Number Using Array V1
Function Date    :  14 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

from array import *

#====================
#
# Entry Point 
#
#====================

def main():
    
    arr = array('i', []) # Empty Array, i for integer
    print(type(arr)) # Display The Type

    iNo1 = int(input("\nEnter Number Of Elements : "))

    for i in range(iNo1):
        arr.append(int(input("\nEnter The Elements : ")))

    print("\nLength / Total Index Of Array Are : ", len(arr))
    print("\nArray Elements Are : ")

    for i in range(len(arr)): # Display The Elements
        print(arr[i])

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()


'''

Using For each loop like java

for No in arr:
    print(No)

using while loop

iCnt = 0
while iCnt < len(arr):
    print(arr[iCnt])
    iCnt += 1

'''
