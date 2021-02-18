'''

Function Name : Count_Digit()
Description   : Calling Count_Digit Function From Main To Find The Digits In The Number From User 
Author        : Prasad Vijaykumar Dangare
Date          : 18-02-2021 

'''


def Count_Digit(iNo):
    iValue = 0
    while (iNo > 0):
        iNo = iNo // 10
        iValue = iValue + 1
    return iValue

def main():
    Number = int(input("Enter The Number : "))
    iRet = Count_Digit(Number)
    print("Digits In The Input is ",iRet)

if __name__ == "__main__":
    main()