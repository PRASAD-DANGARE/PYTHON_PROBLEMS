'''

Function Name : --
Description   : Accepts File Name From User & Check Whether That File Exists In Current Directory Or Not
Author        : Prasad Vijaykumar Dangare
Date          : 27 Mar 2021

'''

import os, sys

fname = input("Enter Filename : ")

if os.path.isfile(fname):
    print(fname + " File Exists")
else:
    print(fname + " does not exist")
    sys.exit()
