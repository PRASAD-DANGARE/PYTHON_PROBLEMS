'''

Function Name : ChkPrime(), MarvellousNum(), ListPrime()
Description   : Accept N Numbers From User As List & Find The Prime Numbers From List & Add All Prime Numbers 
Author        : Prasad Vijaykumar Dangare
Date          : 22 Feb 2021

'''

def ChkPrime(iNo):

    if iNo == 1: 
        return False
    elif iNo == 2: 
        return True 
    else:
        for iRet in range(2, iNo): 
            if iNo % iRet == 0: 
                return False
        return True

def MarvellousNum(arr):
    brr = []
    
    for i in range(len(arr)):
        if ChkPrime(arr[i]) == True:
            brr.append(arr[i])
    
    return brr

def ListPrime(arr2):
    sum = 0
    for i in range(len(arr2)):
        sum = sum + arr2[i]

    return sum

def main():
    
    arr = []
    
    size = int(input("Enter Number Of Elements You Want : "))

    for i in range(size):
        iNo = int(input("Enter Numbers : "))
        arr.append(iNo)

    print("The List Is : ", arr)
    
    newdata = MarvellousNum(arr)
    print("Prime Numbers Are : ", newdata)    

    output = ListPrime(newdata)
    print("Addition Of All Prime Numbers : ", output)    
    
if __name__ == "__main__":
    main()
