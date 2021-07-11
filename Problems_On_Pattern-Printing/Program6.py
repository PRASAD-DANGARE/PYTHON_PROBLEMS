'''
Function Name    :  Pattern
Description      :  Accept Number & Display Character Using Linear Pattern Printing
Function Date    :  11 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Char

'''

#============================
#
# Pattern Operation
#
#============================

def Pattern(iValue1):

    Char = 65

    if iValue1 > 26:
        exit("Invalid Input! | Note : Please Give Input In Between 1 To 26")

    print("\n")

    for _ in range(0, iValue1):
        Ch = chr(Char)
        print(Ch, end = " ")
        Char += 1
        
    print("\n")


#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))

    Pattern(iNo1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()

'''

Input  : 5
Output : A B C D E
'''
