'''
Function Name    :  Check_Prime
Description      :  Accept Number From User And Check Whether It Is Prime Or Not
Function Date    :  05 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Check_Prime Operation
#
#============================

def Check_Prime(iValue1):

    if iValue1 == 1: 
        return False
    
    elif iValue1 == 2: 
        return True 
    
    else:
        for iCnt in range(2, iValue1): 
            if iValue1 % iCnt == 0: 
                return False
        return True

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    bRet = Check_Prime(iNo1)

    if bRet == True:
        print(iNo1, "Is Prime Number")

    else:
        print(iNo1, "Is Not A Prime Number")

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
