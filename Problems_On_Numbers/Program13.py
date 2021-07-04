'''
Function Name    :  Factorial
Description      :  Accept Number From User & Find The Factorial Using Whileloop
Function Date    :  04 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Factorial Operation
#
#============================

def Factorial(iValue1):
    
    if iValue1 <= 0:
        exit("Invalid Input!")

    iMult = 1
    iCnt = iValue1
    
    while iCnt != 0:
        iMult = iMult * iCnt
        iCnt -= 1

    return iMult

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    iRet = Factorial(iNo1)

    print("Factorial Of {0} Are : {1}".format(iNo1, iRet))

#====================
#
# Code Starter
#
#====================
    
if __name__ == "__main__":
    main()
