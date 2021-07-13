'''
Function Name    :  Pattern
Description      :  Accept Row & Column And Display Triangle V2
Function Date    :  11 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''


'''

A-Z = 65 - 90
a-z = 97 - 122
0-9 = 48 - 57

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
    
    for i in range(0, iRow):
        
        Char = 65

        for j in range(0, iCol):

            if i >= j:
                Ch = chr(Char)
                print(Ch, end = "\t")
                Char += 1
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

A       B

A       B       C        

A       B       C       D

'''
