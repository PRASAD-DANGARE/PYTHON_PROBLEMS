'''
Function Name    :  NumberLine
Description      :  Accept Number From User And Display Number Line From Negative To Positive
Function Date    :  10 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# NumberLine Operation
#
#============================

def NumberLine(iValue1):

    if iValue1 < 0:
        iValue1 =- iValue1

    print("\n")
    for iCnt in range(-iValue1, iValue1 + 1):
        print(iCnt)
    print("\n")

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    NumberLine(iNo1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
