'''
Function Name    :  Toggel
Description      :  Accept String From User And Convert Upper Case Letter Into Lower Case Letter
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
    
    #No = len(value1)
    for i in range(len(value1)):
 
        if value1[i] >= 'A' and value1[i] <= 'Z':
            value1[i] = chr(ord(value1[i]) + 32) # ord = unicode, accept 1 input, eg ord("a") = 97, + 32 for lower case

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
    
    print("\nUpdated String Into Lower Case is : ")

    Output = Empty_str.join(Ret)
    print(Output)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
