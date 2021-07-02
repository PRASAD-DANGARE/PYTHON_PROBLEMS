'''
Function Name    :  Display
Description      :  Accept Number From User And Print The List Of Integers From 1 Through N As A String, Without Spaces
Function Date    :  02 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#====================
#
# Display Operation
#
#====================

def Display(iValue1):

    for iCnt in range(1, iValue1 + 1, 1):
        print(iCnt, end = "")

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))
    Display(iNo1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
