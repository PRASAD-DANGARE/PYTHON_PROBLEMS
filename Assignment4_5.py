'''

Function Name : Prime_Number(), Multiply_By_Two(), Maximum_Number()
Description   : Accept N Numbers From User, 
                (Filter) Prime Numbers Then, (Map) Multiply By 2 All Prime Numbers Then, (Reduce) The Maximum Number From List
                
                The List Is :  [2, 70, 11, 10, 17, 23, 31, 77]
                After Filter Prime Numbers :  [2, 11, 17, 23, 31]
                Multiply Prime Number By 2 :  [4, 22, 34, 46, 62]
                Maximum Number From Above List :  62 
                
Author        : Prasad Vijaykumar Dangare
Date          : 24 Feb 2021

'''   

from functools import*

def Prime_Number(iNo):
    if iNo == 1:
        return False
    elif iNo == 2:
        return True
    else:
        for i in range(2, iNo):
            if iNo % i == 0:
                return False
        return True

def Multiply_By_Two(no):
    return no * 2

def Maximum_Number(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2


def main():

    arr = []

    size = int(input("Enter Number Of Elements : "))

    for i in range(size):

        iNo = i + 1
        iNo = int(input("Enter Numbers : "))
        arr.append(iNo)

    print("The List Is : ", arr)

    Filtering = list(filter(Prime_Number, arr)) 
    print("After Filter Prime Numbers : ", Filtering)    

    Mapping = list(map(Multiply_By_Two, Filtering))
    print("Multiply Prime Number By 2 : ", Mapping)

    Reducing = reduce(Maximum_Number, Mapping)
    print("Maximum Number From Above List : ", Reducing)    
    

if __name__ == "__main__":
    main()