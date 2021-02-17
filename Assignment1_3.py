'''

Function Name : Add()
Description   : Calling The Add Function From Main To Perform Addition Of Two Numbers
Author        : Prasad Vijaykumar Dangare
Date          : 17-02-2021 

'''


def Add(iNo1, iNo2): 
    iRet = 0
    iRet = iNo1 + iNo2 # Perform Addition 
    return iRet

def main():
    iNum1 = int(input("Enter One Number : "))
    iNum2 = int(input("Enter Second Number : "))

    Addition = Add(iNum1, iNum2) # Calling The Add Function 

    print("Addition Of {} And {} Is {}".format(iNum1, iNum2, Addition))

if __name__ == "__main__":
    main()