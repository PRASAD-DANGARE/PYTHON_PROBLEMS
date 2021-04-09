'''

Function Name : main()
Description   : Accept Two File Names In Command Line From User & Compare Contents Of Both Files 
                If Both Files Contains Same Display Success Otherwise Display Failure

Author        : Prasad Vijaykumar Dangare
Date          : 27 Mar 2021

'''

import sys
import os.path

def main():

    File1 = open("Assignment9_4.py", "r")
    File2 = open("Assignment9_4.py", "r")

    Flag = False
    for Content1 in File1:
        for Content2 in File2:
            if Content1 == Content2:
                pass
            else:
                print("file is not equal")
                Flag = True
            break

    File1.close()
    File2.close()

    if Flag == False:
        print("file content are same")

if __name__=="__main__":
    main()