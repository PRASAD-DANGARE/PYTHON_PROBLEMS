'''
Function Name    :  Display_Table
Description      :  Accept Number From User & Display Tables Of That Number
Function Date    :  03 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Display Table Operation
#
#============================

def Display_Table(iValue1):

    if iValue1 <= 0:
        return print("Invalid Number!")

    for iCnt in range(1, 11, 1):
        print(iCnt * iValue1)

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    Display_Table(iNo1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
