'''

Function Name : Divisible_By_Five()
Description   : Calling The Divisible_By_Five Function From Main To Check Whether Given Number Is Divisible By 5 Or Not 
Author        : Prasad Vijaykumar Dangare
Date          : 17-02-2021 

'''


def Divisible_By_Five(iNum):
    if iNum % 5 == 0: # Condition
        return True
    else:
        return False

def main():

    iValue = (int(input("Enter One Number : ")))
    iRet = Divisible_By_Five(iValue) # Calling Divisible_By_Five Function

    if iRet == True:
        print("{} Is Divisible By 5 ".format(iValue))
    else:
        print("{} Is Not Divisible By 5 ".format(iValue))

if __name__ == "__main__":
    main()
