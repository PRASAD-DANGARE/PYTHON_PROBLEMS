'''
Function Name    :  Check_Result
Description      :  Accept Marks From User & Check Whether Marks Is In Which Class(Fail, Pass, Second Class, First Class, Distinction)
Function Date    :  02 July 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

#============================
#
# Check Result Operation
#
#============================

def Check_Result(iMarks):
    
    if iMarks < 0 or iMarks > 100:
        return print("Invalid Marks!")

    elif iMarks >= 0 and iMarks < 35:
        print("You Are Failed...")

    elif iMarks >= 35 and iMarks < 50:
        print("Pass Class...")

    elif iMarks >= 50 and iMarks < 60:
        print("Second Class...")

    elif iMarks >= 60 and iMarks < 75:
        print("First Class...")

    else:
        print("Distinction...")

#====================
#
# Entry Point 
#
#====================

def main():

    iNo1 = int(input("Enter Your Marks : "))
    Check_Result(iNo1)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
