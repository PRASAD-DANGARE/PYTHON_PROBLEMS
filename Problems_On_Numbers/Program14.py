'''
Function Name    :  Factors
Description      :  Accept Number From User & Find The Factors Of That Number
Function Date    :  04 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Factors Operation
#
#============================

def Factors(iValue1):
    
    if iValue1 <= 0:
        exit("Invalid Input!")

    for iCnt in range(1, iValue1):
        if iValue1 % iCnt == 0:
            print(iCnt)

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    Factors(iNo1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
