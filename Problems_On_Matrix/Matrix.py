'''

Function Name    :  Matrix_Star
Description      :  Accept Row And Column From User And Display * In Matrix
Function Date    :  07 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int
Output           :  Int

'''

#=======================
#
# Matrix Star Operation
#
#=======================

def Matrix_Star(iRow, iCol):
    
    print("\n")
    
    for _ in range(1, iRow + 1):

        for _ in range(1, iCol + 1):
            
            print(" ", end = "*\t")
        
        print("\n")

#=======================
#
# Entry Point
#
#=======================

def main():

    iNo1 = int(input("Enter Number Of Rows : "))
    iNo2 = int(input("Enter Number Of Columns : "))

    Matrix_Star(iNo1, iNo2)

#=======================
#
# Code Starter
#
#=======================

if __name__ == "__main__":
    main()
