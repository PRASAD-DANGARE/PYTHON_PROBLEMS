'''

Function Name : Pattern_Printing()
Description   : Calling Pattern_Printing Function From Main To Get Input From User & Display That Input In Left Flag Format 
Author        : Prasad Vijaykumar Dangare
Date          : 18-02-2021 

'''

def Pattern_Printing(iNum):
    for iNo1 in range(iNum + 1, 0, -1): 
        for iNo2 in range(0, iNo1 - 1):
            print("*", end = "  ")
        print(" ")

def main():
    value = int(input("\nEnter One Number : "))
    Pattern_Printing(value)

if __name__ == "__main__":
    main()

