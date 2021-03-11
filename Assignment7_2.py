'''

Class Name    : BankAccount
Function Name : Display(), Deposit(), Withdraw(), CalculateInterest()
Description   : Accept Name & Amount And Perform Deposit, Withdraw
Author        : Prasad Vijaykumar Dangare
Date          : 10 Mar 2021

'''

import sys

class BankAccount:

    ROI = 10.5

    def __init__(self, name, Amount):
        self.name = name
        self.Amount = Amount


    def Display(self):

        return self.name, self.Amount
    
    def Deposit(self, Deposit):
        
        self.Amount += Deposit
        return self.Amount
    
    def Withdraw(self, Withdraw):

        self.Amount -= Withdraw
        return self.Amount

    def CalculateIntrest(self, Time):
        
        interest = (self.Amount * Time * BankAccount.ROI) / 100
        return interest

def main():

    name = (input("Enter Account Holder Name : "))
    amount = float(input("Enter The Amount : "))

    obj1 = BankAccount(name, amount)

    while(True):

        print('\n D - Deposit, W - Withdraw, E - Exit')
        choice = input('\n Select One Option : ')

        if choice == 'e' or choice == 'E':
            sys.exit()
        
        amount2 = float(input('\n Enter Amount : '))
    
        if choice == 'd' or choice == 'D':

            print('\n Balance After Deposit : ', obj1.Deposit(amount2))
        
        elif choice == 'w' or choice == 'W':

            print('\n Balance After Withdrawal : ', obj1.Withdraw(amount2))

if __name__=="__main__":
    main()