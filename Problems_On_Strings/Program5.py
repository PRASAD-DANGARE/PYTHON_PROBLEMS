'''
Function Name    :  Length
Description      :  Accept String & Display The String Length
Function Date    :  16 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Length Operation
#
#===============================

def Length(value1):

    print("Length Of String is : ", len(value1))

#====================
#
# Entry Point 
#
#====================

def main():

    str_value = input("Enter The String : ")

    Length(str_value)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
