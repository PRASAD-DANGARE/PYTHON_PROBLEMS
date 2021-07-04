'''
Function Name    :  Add_Factors
Description      :  Accept Number From User & Find The Factors And Perform Addition Of That Numbers
Function Date    :  04 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Add_Factors Operation
#
#============================

def Add_Factors(iValue1):
    
    if iValue1 <= 0:
        exit("Invalid Input!")

    iSum = 0

    for iCnt in range(1, iValue1):

        if iValue1 % iCnt == 0:
            print(iCnt)
            iSum = iSum + iCnt

    return iSum

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    iRet = Add_Factors(iNo1)

    print("Summation Of All Factors Is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()

