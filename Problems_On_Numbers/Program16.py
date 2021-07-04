'''
Function Name    :  Check_Perfect
Description      :  Accept Number From User & Check Whether It Is Perfect Or Not
Function Date    :  04 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Check_Perfect Operation
#
#============================

def Check_Perfect(iValue1):
    
    if iValue1 <= 0:
        exit("Invalid Input!")

    iSum = 0

    for iCnt in range(1, iValue1):

        if iValue1 % iCnt == 0:
            iSum = iSum + iCnt

    if iSum == iValue1:
        return True

    else:
        return False

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    bRet = Check_Perfect(iNo1)

    if bRet == True:
        print(iNo1, "Is Perfect Number")

    else:
        print(iNo1, "Is Not A Perfect Number")

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
