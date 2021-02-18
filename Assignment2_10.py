'''

Function Name : Addition_of_digits()
Description   : Calling Addition_of_Digit Function From Main To Get The Number As Digit In Array And Add The Digit Number 
Author        : Prasad Vijaykumar Dangare
Date          : 18-02-2021 

'''

def Addition_of_digits(iNo):

    ivalue = 0 # Starts With 0
    
    for i in range(len(iNo)):
        ivalue = ivalue + iNo[i] # Adding The Number 
    return ivalue

def main():
    
    Array_Number = [] 

    value = int(input("Enter The Elements For Addition : "))
    
    for i in range(value):

        value = int(input("Enter The Number : "))
        Array_Number.append(value) # Add Each Number At The End

    print("Accepted Number Is : ",Array_Number)

    iRet = Addition_of_digits(Array_Number) # Calling Addition_of_digits Function 
    
    print("Addition Of All Number Is : ",iRet)

if __name__ == "__main__":
    main()