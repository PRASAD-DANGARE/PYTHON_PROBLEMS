'''

Function Name : Number_1_50(), Number_50_1()
Description   : Display Number From 1 To 50 And 50 To 1 In Reverse
Author        : Prasad Vijaykumar Dangare
Date          : 19 Mar 2021

'''

import threading

def Number_1_50():

    for i in range(1, 51):
        print("Numbers From 01 To 50 : ", i)
    print("\n")

def Number_50_1():
    for i in range(50, 0, -1):
        print("Numbers From 50 To 01 : ", i)

def main():

    thread1 = threading.Thread(target = Number_1_50, args = ())
    thread2 = threading.Thread(target = Number_50_1, args = ())

    thread1.start()
    thread1.join()
    thread2.start()

if __name__ == "__main__":
    main()