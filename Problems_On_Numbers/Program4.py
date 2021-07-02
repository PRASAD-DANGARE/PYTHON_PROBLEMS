'''
Function Name    :  is_leap
Description      :  Accept Year From User And Check It Is Leap Year Or Not
Function Date    :  02 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#====================
#
# Leap Year Operation
#
#====================


def is_leap(Year):

    if Year % 100 == 0 or Year % 400 == 0 or Year % 4 == 0:
        return True

    else:
        return False

#====================
#
# Entry Point 
#
#====================

def main():

    Year = int(input("Enter The Year : "))

    print(is_leap(Year))

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
