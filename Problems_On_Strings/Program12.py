'''
Function Name    :  Toggel
Description      :  Accept String From User And Convert lower case to upper case letters
Function Date    :  17 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Convert Into Lower Case Operation
#
#===============================

def Toggel(value1):
    
    if value1 == None:
        exit()

    for i in range(len(value1)):
 
        if value1[i] >= 'a' and value1[i] <= 'z':
            value1[i] = chr(ord(value1[i]) - 32) # - 32 for upper case

#====================
#
# Entry Point 
#
#====================

def main():
    
    Empty_str = ''

    str_value = input("Enter The String : ")
    
    Ret = list(str_value)
 
    Toggel(Ret)
    
    print("\nUpdated String Into Upper Case is : ")

    Output = Empty_str.join(Ret)
    print(Output)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
