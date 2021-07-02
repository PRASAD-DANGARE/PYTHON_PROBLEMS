'''
Function Name    :  Maximum
Description      :  Accept 2 Numbers From User And Find Maximum Number  
Function Date    :  02 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

#====================
#
# Maximum Operation
#
#====================

def Maximum(iValue1, iValue2):

    if(iValue1 > iValue2):
        return iValue1

    else:
        return iValue2

#====================
#
# Entry Point Function
#
#====================

def main():

    iNo1 = int(input("Enter First Number : "))
    iNo2 = int(input("Enter Second Number : "))

    iRet = Maximum(iNo1, iNo2)

    print("Maximum Number Is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
