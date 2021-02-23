'''

Function Name : Addition()
Description   : Accept N Numbers From User As List & Perform Addition Of That Numbers 
Author        : Prasad Vijaykumar Dangare
Date          : 22 Feb 2021

'''

def Addition(iNo):

    Ans = 0 
    for i in range(len(iNo)): 
        Ans = Ans + iNo[i]
    return Ans

def main():
    
    arr = []

    value = int(input("Enter Number Of Elements You Want : "))
    for i in range(value):
        value = i + 1
        value = int(input("Enter Numbers : "))
        arr.append(value)

    ret = Addition(arr) # Function Call

    print("Addition of Numbers Is : ", ret)


if __name__ == "__main__":
    main()

