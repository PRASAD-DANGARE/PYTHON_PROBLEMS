'''

Function Name : ChkNum()
Description   : Calling The ChkNum Function From Main Whether Number Is Odd or Even
Author        : Prasad Vijaykumar Dangare
Date          : 17-02-2021 

'''


def ChkNum(iNo1):
    if iNo1 % 2 == 0: # Condition 
        return True
    else:
        return False # Return Type is Boolean

def main():

    value = (int(input("Enter One Number : ")))
    Bret = ChkNum(value) # Boolean Type, Calling ChkNum

    if Bret == True:
        print("{} is Even ".format(value))
    else:
        print("{} is Odd ".format(value))

if __name__ == "__main__": 
    main()