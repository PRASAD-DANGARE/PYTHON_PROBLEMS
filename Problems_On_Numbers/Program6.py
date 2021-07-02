'''
Function Name    :  Check_Even
Description      :  Accept Number From User And Check It Is Even Or Not
Function Date    :  02 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Check Even Number Operation
#
#============================

def Check_Even(iValue1):
    
    if iValue1 % 2 == 0:
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
    bRet = Check_Even(iNo1)

    if(bRet == True):
        print(iNo1, "Is Even Number ")

    else:
        print(iNo1, "Is Not An Even Number ")

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
