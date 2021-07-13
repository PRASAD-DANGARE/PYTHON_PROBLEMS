'''
Function Name    :  Pattern
Description      :  Accept Row & Column And Display Triangle V3
Function Date    :  11 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

#============================
#
# Pattern Operation
#
#============================

def Pattern(iRow, iCol):

    if iRow != iCol:
        exit("Invalid Input! | Note : Give Input Same As Row & Column")

    print("\n")
    
    Char = 65

    for i in range(0, iRow):
        Ch = chr(Char)
        Char += 1
        
        for j in range(0, i + 1):

            if i >= j:
                print(Ch, end = "\t")
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

Enter Number Of Rows : 4
Enter Number Of Columns : 4


A

B       B

C       C       C

D       D       D       D

'''
