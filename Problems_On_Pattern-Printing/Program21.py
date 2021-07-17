'''
Function Name    :  ASCII_Table
Description      :  Display ASCII Table
Function Date    :  17 July 2021
Function Author  :  Prasad Dangare
Input            :  ----
Output           :  ----

'''

#===============================
#
# Display ASCII Table Operation
#
#===============================

def ASCII_Table():

    print("---------------------\n")
    print("-----ASCII TABLE-----\n")
    print("---------------------\n")

    for i in range(128):
        ch = chr(i)
        #print(i, "\t\t", ch)
        print("Value = ", i, " : ", ch)

    print("---------------------\n")

#====================
#
# Entry Point 
#
#====================

def main():

    ASCII_Table()

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
