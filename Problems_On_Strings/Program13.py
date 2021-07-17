'''
Function Name    :  Toggel_Both
Description      :  Accept String From User And toggle uppercase letter to lowercase letter
Function Date    :  17 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#===============================
#
# Toggel Operation
#
#===============================

def Toggel_Both(value1):
    
    if value1 == None:
        exit()

    for i in range(len(value1)):
 
        if value1[i] >= 'a' and value1[i] <= 'z':
            value1[i] = chr(ord(value1[i]) - 32)

        elif value1[i] >= 'A' and value1[i] <= 'Z':
            value1[i] = chr(ord(value1[i]) + 32)

#====================
#
# Entry Point 
#
#====================

def main():
    
    Empty_str = ''

    str_value = input("Enter The String : ")
    
    Ret = list(str_value)
 
    Toggel_Both(Ret)
    
    print("\nUpdated String is : ")

    Output = Empty_str.join(Ret)
    print(Output)

#====================
#
# Code Starter
#
#====================

if __name__ == "__main__":
    main()
