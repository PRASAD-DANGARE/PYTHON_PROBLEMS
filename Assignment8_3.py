'''

Function Name : Even_List(), Odd_List()
Description   : Accept List From User & Display Addition Even & Odd Numbers
Author        : Prasad Vijaykumar Dangare
Date          : 19 Mar 2021

'''

import threading

def Even_List(No1):

    No1 = list(No1)
    Ans = 0
    
    for i in range(len(No1)):
        if  No1 [i] % 2 == 0:
            Ans = Ans + No1[i]

    print("Addition Of Even Numbers Are : ", Ans)

def Odd_List(No2):

    No2 = list(No2)
    Ans2 = 0

    for i in range(len(No2)):
        if No2 [i] % 2 != 0:
            Ans2 = Ans2 + No2[i]

    print("Addition Of Odd Numbers Are : ", Ans2)

def main():
    
    arr = []

    value = int(input("Enter How Many Elements : ")) 
    
    for i in range(value):
        value = i + 1
        iNo = int(input("Enter Numbers : "))
        arr.append(iNo)

    thread1 = threading.Thread(target = Even_List, args = (arr,))
    thread2 = threading.Thread(target = Odd_List, args = (arr,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    print("Exit From Main.")

if __name__ == "__main__":
    main()