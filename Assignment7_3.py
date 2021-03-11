'''

Class Name    : Numbers
Function Name : Accept(), Factors(), Summation(), ChkPerfect(), ChkPerfect(), ChkPrime()
Description   : Accept Number From User & Find Summation,Even,Perfect,Prime,Factors 
Author        : Prasad Vijaykumar Dangare
Date          : 10 Mar 2021

'''

# Calculate The Summation Of All Numbers 
# Display All Even Numbers
# Display All Perfect Number 
# Display All Prime Numbers
# Display All Factors 

class Numbers:
    
    def __init__(self, no = 10): 
        self.size = no 
        self.arr = []
        
    def Accept(self):
        for i in range(self.size):
            iNo = int(input("Enter Number : "))
            self.arr.append(iNo)
            
    def Factors(self):
        x = self.size
        arr = []
 
        for i in range(1, x + 1):
            if x % i == 0:
                arr.append(i)
        return arr

    def Summation(self):
        sum = 0
        for i in range(self.size):
            sum = sum + self.arr[i]
        return sum

    def ChkPerfect(self):
        sum = 0
        for i in range(self.size):
            for j in range(1, int(self.arr [i] / 2) + 1):
                if(self.arr [i] % j) == 0:
                    sum = sum + j
            if sum == self.arr [i]:
                print(self.arr [i])
            sum = 0

    def ChkPrime(self):
        Flag = False
        for i in range(self.size):
            for j in range(2, int(self.arr [i] / 2) + 1):
                if(self.arr [i] % j) == 0:
                    Flag = True
                break
            if Flag == False:
                print(self.arr [i])
            Flag = False

def main():

    value = int(input("Enter Number Of Elements : "))
    obj1 = Numbers(value)

    obj1.Accept()

    print("\nPrime numbers are : ")
    obj1.ChkPrime()

    arr = obj1.Factors()
    print("\nfactors are : {}".format(arr))

    ret = obj1.Summation()
    print("\nSummation of all elements :", ret)
    
    print("\nPerfect numbers are : ")
    obj1.ChkPerfect()

if __name__ == "__main__":
    main()