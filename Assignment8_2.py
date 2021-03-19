'''

Function Name : Even_Factors(), Odd_Factors()
Description   : Accept Number From User & Display Even & Odd Factors 
Author        : Prasad Vijaykumar Dangare
Date          : 19 Mar 2021

'''

import threading

def Even_Factors(No1):
    Ans = 0
    for i in range(1, No1):
        if i % 2 == 0:
            Ans = Ans + i
    print("Addition Of Even Numbers : ", Ans)

def Odd_FactorS(No2):
    Ans2 = 0
    for i in range(1, No2):
        if i % 2 != 0:
            Ans2 = Ans2 + i
    print("Addition Of Odd Numbers : ", Ans2)


def main():

    num = int(input("Enter The Number : "))
    thread1 = threading.Thread(target = Even_Factors, args = (num,))
    thread2 = threading.Thread(target = Odd_FactorS, args = (num,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit From Main.")

if __name__ == "__main__":
    main()