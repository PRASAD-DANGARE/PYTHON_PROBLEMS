'''

Function Name    :  Matrix
Description      :  Accept Row, Column And Elements From User And Display The Matrix
Function Date    :  07 July 2021
Function Author  :  Prasad Dangare
Input            :  Int, Int, Int
Output           :  Int

'''

#=======================
#
# Matrix Operation
#
#=======================

def Matrix(iRow, iCol):

    Matrix = []
    print("\nEnter The Elements : \n")

    for i in range(iRow):
        a = []
        for j in range(iCol):
            
            a.append(int(input()))
        Matrix.append(a)    

    print("\nMatrix is : ")

    print("\n")

    for i in range(iRow):
        for j in range(iCol):
    
            print(Matrix[i][j], end = "\t")
        print("\n")

#=======================
#
# Entry Point
#
#=======================

def main():

    iNo1 = int(input("\nEnter Number Of Rows : "))
    iNo2 = int(input("Enter Number Of Columns : "))

    Matrix(iNo1, iNo2)

#=======================
#
# Code Starter
#
#=======================

if __name__ == "__main__":
    main()