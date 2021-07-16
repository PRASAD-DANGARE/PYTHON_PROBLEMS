'''
Function Name    :  Display
Description      :  Accept String & Display The String On Screen V2
Function Date    :  16 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Display Operation
#
#===============================

def Display(value1):

    print("String Is : ", value1)

#====================
#
# Entry Point 
#
#====================

def main():

    str_value = input("Enter Your Name : ")

    Display(str_value)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
