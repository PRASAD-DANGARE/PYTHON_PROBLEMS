'''
Function Name    :  Count_Small
Description      :  Accept String & Count The Small Letters
Function Date    :  16 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Count Small Letters Operation
#
#===============================

def Count_Small(value1):

    iCnt = 0

    if value1 == None:
        exit("Invalid Input!")

    for i in value1:

        if i >= 'a' and i <= 'z':
            iCnt += 1

    return iCnt

#====================
#
# Entry Point 
#
#====================

def main():

    str_value = input("Enter The String : ")

    iRet = Count_Small(str_value)

    print("Frequency Of Small Letters is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
