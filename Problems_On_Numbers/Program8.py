'''
Function Name    :  Check_Division
Description      :  Accept 2 Number From User & Check Both Are Divisible By Each Other Or Not 
Function Date    :  02 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

#============================
#
# Check Divisible Operation
#
#============================

def Check_Division(iValue1, iValue2):
    
    if iValue1 % iValue2 == 0:
        return True

    else:
        return False

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter First Number : "))
    iNo2 = int(input("Enter Second Number : "))

    bRet = Check_Division(iNo1, iNo2)

    if(bRet == True):
        print("Yes First Number Is Divisible By Second Number")

    else:
        print("No First Number Is Not Divisible By Second Number")

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
