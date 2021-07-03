'''
Function Name    :  Power
Description      :  Accept Number From User & Calculate its power
Function Date    :  03 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Calculating Power Operation
#
#============================

def Power(iValue1, iValue2):

    if iValue1 <= 0 or iValue2 <= 0:
        exit("Invalid Input!")
        
    iMult = 1

    for _ in range(1, iValue2 + 1):
        iMult = iMult * iValue1

    return iMult

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))
    iNo2 = int(input("Enter Power For That Number : "))

    iRet = Power(iNo1, iNo2)

    #print("Result is : ", iRet)
    print("Result of {0} Power ^ {1} Is : {2}".format(iNo1, iNo2, iRet))

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
