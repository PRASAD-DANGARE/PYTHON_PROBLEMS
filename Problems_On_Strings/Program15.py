'''
Function Name    :  Display
Description      :  Accept String From User And Display It In Reverse Order
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

    for i in value1:
        Empty_str = i + Empty_str

    return Empty_str

#====================
#
# Entry Point 
#
#====================

def main():

    str_value = input("Enter The String : ")

    Ret = Display(str_value)

    print("Original String is : ", str_value)
    print("Reversed String is : ", Ret)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
