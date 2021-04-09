'''

Function Name : main()
Description   : Accept File Name From User & Open That File & Display The Contents Of That File On Screen
Author        : Prasad Vijaykumar Dangare
Date          : 27 Mar 2021

'''

def main():

    name = input("Enter the file name that you want to Read : ")
    
    fobj = open(name,"r")   # create new file
    
    print("Data from file is : \n")
    print(fobj.read())
    
if __name__ == "__main__":
    main()
