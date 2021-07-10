'''
Function Name    :  Pattern
Description      :  Accept Number & Display Character That Number Of Times Using Linear Pattern Printing
Function Date    :  10 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Str
Output           :  str

'''

#============================
#
# Pattern Operation
#
#============================

def Pattern(iValue1, ch):

    if len(ch) > 1:
        exit("Invalid Input! | Note : Give Input In Single Character")

    print("\n")
    for _ in range(iValue1, 0, -1):
        print(ch, end = " ")
    print("\n")

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))
    Char1 = str(input("Enter The Character : "))

    Pattern(iNo1, Char1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()

'''

Input  : 5
Output : p p p p p

'''
