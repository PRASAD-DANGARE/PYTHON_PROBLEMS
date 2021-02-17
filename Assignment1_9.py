'''

Function Name : Even_Number()
Description   : Calling Even_Number Function From Main To Find The Even Number From Maximum Number
Author        : Prasad Vijaykumar Dangare
Date          : 17-02-2021 

'''

def Even_Number(iNum): 
    for iNum in range(1, iNum + 1): # 1 is the starting point otherwise it start with 0, +1 is the count after each number
        if iNum %2 == 0: # condition
            print(iNum, end = " ") # display in the same line

def main():
    value = int(input("Enter The Max Number : "))
    Even_Number(value) # Calling Even_Number Function

if __name__ == "__main__":
    main()

