'''
Function Name    :  Display
Description      :  Accept String From User And Display It In Reverse Order V2
Function Date    :  17 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Reverse Display Operation
#
#===============================

def Display(value1):

    Empty_str = ""

    iCnt = len(value1)
    
    while iCnt > 0:

        Empty_str += value1[iCnt - 1]
        iCnt -= 1

    print("Original String is : ", value1)
    print("Reversed String is : ", Empty_str)

#====================
#
# Entry Point 
#
#====================

def main():

    str_value = input("Enter The String : ")

    Display(str_value)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
