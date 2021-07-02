'''
Function Name    :  Check_Division
Description      :  Accept Number From User & Check It Is Divisible By 3 And 5
Function Date    :  02 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''
#============================
#
# Check Divisible Operation
#
#============================

def Check_Division(iValue1):
    
    if iValue1 % 3 == 0 and iValue1 % 5 == 0:
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
    bRet = Check_Division(iNo1)

    if(bRet == True):
        print(iNo1, "Is Divisible By 3 And 5")

    else:
        print(iNo1, "Is Not Divisible By 3 And 5")

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
