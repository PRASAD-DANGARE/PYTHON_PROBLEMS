'''
Function Name    :  Count_Space
Description      :  Accept String & Count The White Spaces
Function Date    :  16 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Count White Spaces Operation
#
#===============================

def Count_Spaces(value1):

    iCnt = 0

    if value1 == None:
        exit("Invalid Input!")

    for i in value1:

        if i == ' ':
            iCnt += 1

    return iCnt

#====================
#
# Entry Point 
#
#====================

def main():

    str_value = input("Enter The String : ")

    iRet = Count_Spaces(str_value)

    print("Count Of White Spaces is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
