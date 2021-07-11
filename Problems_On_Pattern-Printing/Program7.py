'''
Function Name    :  Pattern
Description      :  Accept Row & Column And Display * Using Non Linear Pattern Printing
Function Date    :  11 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Special Simbol

'''

#============================
#
# Pattern Operation
#
#============================


def Pattern(iRow, iCol):

    print("\n")

    for i in range(0, iRow):
        for j in range(0, iCol):
            print(end = "*\t")
        
        print("\n")


#====================
#
# Entry Point 
#
#====================


def main():

    iNo1 = int(input("Enter Number Of Rows : "))
    iNo2 = int(input("Enter Number Of Columns : "))

    Pattern(iNo1, iNo2)


#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()

'''

Input  : 3, 3

Output : * * *
         * * *
         * * *
 
'''
