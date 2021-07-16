'''
Function Name    :  Count_A
Description      :  Accept String & Count The Number Of Letters a, A
Function Date    :  16 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Count a, A Operation
#
#===============================

def Count_A(value1):

    iCnt = 0

    if value1 == None:
        exit("Invalid Input!")

    for i in value1:
        if i == 'a' or i == 'A':
            iCnt += 1

    return iCnt

#====================
#
# Entry Point 
#
#====================

def main():

    str_value = input("Enter The String : ")

    iRet = Count_A(str_value)

    print("Count of small a / A is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
