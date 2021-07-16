'''
Function Name    :  Count_a
Description      :  Accept String & Count The Number Of Letters a
Function Date    :  16 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Count Small a Operation
#
#===============================

def Count_a(value1):

    iCnt = 0

    if value1 == None:
        exit("Invalid Input!")

    for i in value1:
        if i == 'a':
            iCnt += 1

    return iCnt

#====================
#
# Entry Point 
#
#====================

def main():

    str_value = input("Enter The String : ")

    iRet = Count_a(str_value)

    print("Count of small a is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
