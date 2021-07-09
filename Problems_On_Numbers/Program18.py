'''
Function Name    :  Difference
Description      :  Find Factors & Non Factors And Subtract Both Factors And Non Factors
Function Date    :  09 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Difference Operation
#
#============================

def Difference(iValue1):

    iSum1 = 0
    iSum2 = 0

    if iValue1 < 0:
        exit("Invalid Input! | Note : Give Input Greater Than 0")

    for iCnt in range(1, iValue1):

        if iValue1 % iCnt == 0:
            #print("Even Factors Are : ", iCnt)
            iSum1 = iSum1 + iCnt

        else:
            #print("Odd Factors Are : ", iCnt)
            iSum2 = iSum2 + iCnt

    print("Even Factors Are : ", iSum1)
    print("Odd Factors Are : ", iSum2)

    return iSum1 - iSum2

#====================
#
# Entry Point 
#
#====================

def main():

    print("Enter The Number : ")
    iNo1 = int(input())

    iRet = Difference(iNo1)

    print("Difference is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()

