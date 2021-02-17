'''

Function Name : Pattern()
Description   : Calling Pattern Function From Main To Display Number Of " * " From User
Author        : Prasad Vijaykumar Dangare
Date          : 17-02-2021 

'''

def Pattern(iNum):
    for i in range(iNum): # Loop to print till the given number
        print(end = "* ")

def main():
    iRet = (int(input("Enter Number Of Columns In * : ")))
    Pattern(iRet) # Calling The Pattern Function
    
if __name__ == "__main__":
    main()