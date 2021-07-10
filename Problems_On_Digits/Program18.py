'''
Function Name    :  Frequency
Description      :  Accept Digit From User And Find The Frequency In Between 3 And 7
Function Date    :  10 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Frequency Operation
#
#============================

def Frequency(iValue1):

    iCnt = 0
    iDigit = 0

    while iValue1 > 0:
        iDigit = iValue1 % 10
        if iDigit >= 3 and iDigit <= 7:
            iCnt += 1
        iValue1 = iValue1 // 10

    return iCnt

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    iRet = Frequency(iNo1)

    print("Frequency In Between 3 And 7 is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
