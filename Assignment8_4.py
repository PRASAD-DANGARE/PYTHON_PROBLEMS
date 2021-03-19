'''

Function Name : Small_Letters(), Capital_Letters(), Digits_Numbers()
Description   : Accept Input From User & Display The Count Of Small Letters, Capital Letters, Digits
Author        : Prasad Vijaykumar Dangare
Date          : 19 Mar 2021

'''

import threading

def Small_Letters(No1):

    Smaller = 0

    for i in range(0, len(No1)):
        if No1 [i].islower():
            Smaller += 1
    print("Small Letters Are : ", Smaller)

def Capital_Letters(No2):

    Capital = 0

    for i in range(0, len(No2)):
        if No2 [i].isupper():
            Capital += 1
    print("Capital Letters Are : ", Capital)
    
def Digit_Numbers(No3):
    
    Digits = 0

    for i in range(0, len(No3)):
        if No3 [i].isdigit():
            Digits += 1
    print("Digits Are : ", Digits)

def main():

    Value = input("Enter Capital Letters, Small Letters & Digits  : ")

    thread1 = threading.Thread(target = Small_Letters, args = (Value,))

    thread2 = threading.Thread(target = Capital_Letters, args = (Value,))

    thread3 = threading.Thread(target = Digit_Numbers, args = (Value,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()