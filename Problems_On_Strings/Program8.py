'''
Function Name    :  Count_Capital
Description      :  Accept String & Count The Capital Letters
Function Date    :  16 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Count Capital Letters Operation
#
#===============================

def Count_Capital(value1):

    iCnt = 0

    if value1 == None:
        exit("Invalid Input!")

    for i in value1:

        if i >= 'A' and i <= 'Z':
            iCnt += 1

    return iCnt

#====================
#
# Entry Point 
#
#====================

def main():

    str_value = input("Enter The String : ")

    iRet = Count_Capital(str_value)

    print("Frequency Of Capital Letters is : ", iRet)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
