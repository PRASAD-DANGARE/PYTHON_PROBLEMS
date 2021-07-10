'''
Function Name    :  Pattern
Description      :  Accept Number From User And Display Number,* In Reverse Order Using Linear Pattern Printing
Function Date    :  10 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Special Simbol

'''

#============================
#
# Pattern Operation
#
#============================

def Pattern(iValue1):

    print("\n")
    for iCnt in range(iValue1, 0, -1):
        print(iCnt, end = "\t*\t")
    print("\n")

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    Pattern(iNo1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()

'''

Input  : 4
Output : 4       *       3       *       2       *       1       *

'''
