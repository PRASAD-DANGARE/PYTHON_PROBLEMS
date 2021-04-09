'''

Function Name : main()
Description   : Accept File Name In Command Line From User & Create New File &
                Copy All Contents From Existing File Into New File

Author        : Prasad Vijaykumar Dangare
Date          : 27 Mar 2021

'''

import sys
import os.path


if len(sys.argv) < 2 :
    print("please give filename using command line")
    exit()

def main():

    if os.path.exists(sys.argv[1]):
        print("file exist")
    else:
        print("file does not exist")

    with open(sys.argv[1]) as f:
        with open("welcome.txt", "w") as f1:
            for line in f:
                f1.write(line)
    f.close()

if __name__=="__main__":
    main()
