'''

Function Name : Even_Number(), Square_Number(), Addition()
Description   : Accept N Numbers From User, 
                (Filter) Even Numbers Then (Map) The Square Even Numbers Then (Reduce) Perform Addition Of That Numbers
                
                The List Is :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
                After Filter Even Numbers :  [2, 4, 4, 2, 8, 10]
                Square Of Even Numbers :  [4, 16, 16, 4, 64, 100]
                Addition Of All Elements :  204
                
Author        : Prasad Vijaykumar Dangare
Date          : 24 Feb 2021
'''

from functools import*

def Even_Number(iNo):
    if iNo % 2 == 0:
        return True
    else:
        return False

def Square_Number(no):
    return no * no

def Addition(no1, no2):
    return no1 + no2


def main():

    arr = []

    size = int(input("Enter Number Of Elements : "))

    for i in range(size):

        iNo = i + 1
        iNo = int(input("Enter Numbers : "))
        arr.append(iNo)

    print("The List Is : ", arr)

    newdata = list(filter(Even_Number, arr)) 
    print("After Filter Even Numbers : ", newdata)    

    newdata1 = list(map(Square_Number, newdata))
    print("Square Of Even Numbers : ", newdata1)

    output = reduce(Addition, newdata1)
    print("Addition Of All Elements : ", output)    
    

if __name__ == "__main__":
    main()

'''

from functools import*

def Even_Number(iNo):
    if iNo % 2 == 0:
        return True
    else:
        return False

def Square_Number(no):
    return no * no

def Addition(no1, no2):
    return no1 + no2


def main():

    arr = []

    size = int(input("Enter Number Of Elements : "))

    for i in range(size):

        iNo = i + 1
        iNo = int(input("Enter Numbers : "))
        arr.append(iNo)

    print("The List Is : ", arr)

    newdata = list(filter(Even_Number, arr)) 
    print("After Filter Even Numbers : ", newdata)    

    newdata1 = list(map(Square_Number, newdata))
    print("Square Of Even Numbers : ", newdata1)

    output = reduce(Addition, newdata1)
    print("Addition Of All Elements : ", output)  

'''