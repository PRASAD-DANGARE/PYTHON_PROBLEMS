'''

Function Name : Even(), Odd()
Description   : Display Even And Odd Number Upto 10
Author        : Prasad Vijaykumar Dangare
Date          : 19 Mar 2021

'''

import threading

def Even():
    for i in range(1, 11):
        if i % 2 == 0:
            print("Even Numbers Are : ", i)
def Odd():
    for i in range(1, 10):
        if i % 2 != 0:
            print("Odd Numbers Are : ", i)

def main():

    thread1 = threading.Thread(target = Even, args = ())
    thread2 = threading.Thread(target = Odd, args = ())

    thread1.start() # It Execute Both Threads Parallel
    thread2.start()

    thread1.join()  # Wait Until Child Process Terminates & Then Return To Parent Process
    thread2.join()

if __name__ == "__main__":
    main()