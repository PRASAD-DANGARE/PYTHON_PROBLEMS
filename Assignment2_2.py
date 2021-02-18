'''

Function Name : Pattern()
Description   : Calling Pattern Function From Main To Display Number Of " * " From User In Tabular Formet
Author        : Prasad Vijaykumar Dangare
Date          : 18-02-2021 

'''

def Pattern(iNum):
    for i in range(iNum): # Outer For Loop
        for j in range(iNum): # Inner For Loop
            print('  ', end = "* ") 
        print() # Display Every Line In Row, Column Eg 5 Row And 5 Column

def main():
    iRet = (int(input("Enter Input Of Type Integer Which Display The * : ")))
    Pattern(iRet) # Calling The Pattern Function
    
if __name__ == "__main__":
    main()