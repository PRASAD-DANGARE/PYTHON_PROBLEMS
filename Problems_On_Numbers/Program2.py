'''
Function Name    :  Display
Description      :  Accept Number From User And Display That All Numbers 
Function Date    :  02 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#====================
#
# Display Operation
#
#====================

def Display(iValue1):

    if(iValue1 < 0):
        iValue1 =- iValue1 # Convert Negative Value Into Positive

    '''while iCnt <= iValue1:
        print(iCnt)
        iCnt = iCnt + 1'''

    for iCnt in range(1, iValue1 + 1, 1):
        print(iCnt)

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter The Number : "))
    Display(iNo1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
