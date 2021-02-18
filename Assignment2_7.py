'''

Function Name : Table_Pattern()
Description   : Calling Table_Pattern Function From Main To Get Input From User & Display That Input In Tabular Format 
Author        : Prasad Vijaykumar Dangare
Date          : 18-02-2021 

'''

def Table_Pattern(iNum):
    for iNo1 in range(1, iNum):
        for iNo2 in range(1, iNum + 1):
            print('{:5}'.format(iNo2, iNo1), end ='') # Each Column Size Is 8
        print()   

def main():
    value = int(input("Enter One Number : "))
    Table_Pattern(value)

if __name__ == "__main__":
    main()