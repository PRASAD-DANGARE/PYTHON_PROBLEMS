'''

Function Name : Recursion_Pattern()
Description   : Accept N Number From User To Print Same Number In Form Of * Using Recursion 
Author        : Prasad Vijaykumar Dangare
Date          : 26 Feb 2021

'''

def Recursion_Pattern(iNo): 
    
    if iNo >= 1:
        no = iNo - 1
        print(end = "* ")
        Recursion_Pattern(no) # Calling Itself And Then Return The Value To Function Call

def main():

    value = int(input("Enter Number To Print * : "))
    Recursion_Pattern(value) # Function Call

if __name__ == "__main__":
    main()

