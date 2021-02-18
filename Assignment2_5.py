'''

Function Name : PRIME()
Description   : Calling PRIME Function From Main To Check Whether Given Number Is Prime Or Not 
Author        : Prasad Vijaykumar Dangare
Date          : 18-02-2021 

'''

def PRIME(iNum):
    if iNum == 1: # Every Prime Number Has Not 1 Factor, And 1 Is Not A Prime Number
        return False
    elif iNum == 2: # Prime Number Has 2 Factors, Prime No Start From 2 And 2 Is The Even Prime Number
        return True 
    else:
        for iRet in range(2, iNum): # If A Number Has 2 Factors Return True, Greater Than 2 And Not Divide By Any Other No 
            if iNum % iRet == 0: # If A Number Has Not 2 Factors Return False, Prime Number Is Not Divisible By Other No
                return False
        return True

def main():
    value = int(input("Enter The Number : "))
    iNo = PRIME(value)

    if iNo == True:
        print("{} is A Prime Number ".format(value, iNo))
    else:
        print("{} is Not A Prime Number ".format(value, iNo))

if __name__ == "__main__":
    main()