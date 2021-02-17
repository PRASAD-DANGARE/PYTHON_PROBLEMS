'''

Function Name : iNumber()
Description   : Calling The iNumber Function From Main To Display 10 To 1 On Screen
Author        : Prasad Vijaykumar Dangare
Date          : 17-02-2021 

'''

def iNumber():
    iNum = 0
    for iNum in range(10,0,-1): # First Is The START Value, Second Is The STOP Value, Third Is STEP For The Value
        print(iNum)

def main():
    iNumber() # Call For iNumber Function

if __name__ == "__main__":
    main()

'''

# Or We Can Also Use List 

def iNumber(List):
    iNum = 0
    for iNum in range(len(List)):
        print(List[iNum])

def main():
    Array_list = [10,9,8,7,6,5,4,3,2,1]
    iNumber(Array_list)

if __name__ == "__main__":
    main()

'''
