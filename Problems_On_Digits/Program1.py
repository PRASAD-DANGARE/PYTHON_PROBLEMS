'''
Function Name    :  Display_Digits
Description      :  Accept Digit From User And Display That Number Separately In Reverse Order
Function Date    :  05 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Display_Digits Operation
#
#============================

def Display_Digits(iValue1):

    if iValue1 <= 0:
        iValue1 =- iValue1

    iDigit = 0

    while iValue1 > 0:

        iDigit = iValue1 % 10
        print(iDigit)
        iValue1 = iValue1 // 10

#====================
#
# Entry Point 
#
#====================

def main():

    iDigit = int(input("Enter The Digits : "))

    Display_Digits(iDigit)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
