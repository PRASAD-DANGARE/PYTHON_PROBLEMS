'''

Function Name : Check_Number()
Description   : Calling The Check_Number Function From Main To Check Whether Given Number Is Positive, Negative, Zero
Author        : Prasad Vijaykumar Dangare
Date          : 17-02-2021 

'''

def Check_Number(iNum):
    if iNum > 0: # Condition
        print("Number Is POSITIVE")

    elif iNum == 0:
        print("Number Is ZERO")

    else:
        print("Number Is NEGATIVE")

def main():

    iNo = int(input("Enter One Number : "))
    Check_Number(iNo) # Calling Check_Number Function

if __name__ == "__main__":
    main()

