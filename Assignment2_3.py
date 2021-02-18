'''

Function Name : FACTORIAL()
Description   : Calling FACTORIAL Function From Main To Display Factorial Of A Number 
Author        : Prasad Vijaykumar Dangare
Date          : 18-02-2021 

'''


def FACTORIAL(iNum):

    iRet = 1 # Start From 1 1x2 etc
    
    for i in range(1, iNum + 1): # Start From 1 And Reference Counter Is Increasing 2,3,4,5
        iRet = iRet * i
    
    if iNum <= 0: # Condition
        print("Number Is Less Than Zero Give More Than 1")
    
    else:
        print("The Factorial Of", iNum, "is", iRet)

def main():
    value = int(input("Enter The Number : "))
    FACTORIAL(value)

if __name__ == "__main__":
    main()
