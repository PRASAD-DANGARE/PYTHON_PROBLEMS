'''

Function Name : Recursion_Addition()
Description   : Accept N Number From User & Ask How Many Elements You Want And Add That Elements 
Author        : Prasad Vijaykumar Dangare
Date          : 26 Feb 2021

'''

Ans = 0
iNum = 0

def Recursion_Addition(data):

    global Ans
    global iNum

    if iNum < len(data):
        Ans = Ans + data[iNum]
        iNum = iNum + 1
        Recursion_Addition(data)
    return Ans

def main():

    iValue = [] 

    size = int(input("Enter Number Of Elements For Addition : "))
    
    for i in range(size):

        value = int(input("Enter The Number : "))
        iValue.append(value) 

    print("Accepted Number Is : ", iValue)

    iRet = Recursion_Addition(iValue) 
    
    print("Addition Of All Number Is : ",iRet)

if __name__ == "__main__":
    main()
