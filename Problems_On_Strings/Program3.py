'''
Function Name    :  Display
Description      :  Accept String & Display The String In Single Line
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

    iCnt = 0

    print("String Are : \n")

    while iCnt < len(value1):
        print(value1[iCnt])
        iCnt += 1

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
