'''

Function Name : Flag_Pattern()
Description   : Calling Flag_Pattern Function From Main To Get Input From User & Display That Input In Flag Format 
Author        : Prasad Vijaykumar Dangare
Date          : 18-02-2021 

'''

def Flag_Pattern(iNo):

    iValue = 1 # Starting Number
    
    for iNo1 in range(0, iNo): # Outer Loop For Number Of Rows
        iValue = 1 
        
        for iNo2 in range(0, iNo1 + 1): # Inner Loop For Number Of Column, Values Changing According To Outer Loop
            
            print(iValue, end = "   ")
            iValue = iValue + 1 # Incrementing Number At Each Column
        
        print("\r") # End After Each Row

def main():

    value = int(input("Enter One Number : "))
    Flag_Pattern(value)

if __name__ == "__main__":
    main()

