'''

Function Name : Marvellous()
Description   : Calling The Marvelous Function From Main To Display 5 Times On Screen
Author        : Prasad Vijaykumar Dangare
Date          : 17-02-2021 

'''

def Marvellous():
    iCnt = 1
    while iCnt <= 5: # Condition 
        print("Marvellous") # Message
        iCnt = iCnt + 1 # Every Time Reference Count Is Increasing 1,2,3,4,5

def main():
    Marvellous() # Call To Marvellous Function

if __name__ == "__main__":
    main()