'''

Function Name : main()
Description   : Accept N Numbers From User As List & Find The Minimum Number From List 
Author        : Prasad Vijaykumar Dangare
Date          : 22 Feb 2021

'''

def main():

    arr = [] # create list
    
    value = int(input("Enter How Many Elements : ")) # get from user
    
    for i in range(value):
        iNo = int(input("Enter Numbers : "))
        arr.append(iNo)

    #print('The List Is : ', arr) # Display The List

    Minimum = arr[0] # Initially 0th Element Becomes Minimum

    for i in range(1, value): # Repeat From 1 To n-1 Elements
        if arr[i] < Minimum: 
            Minimum = arr[i] # If Any Other Elements Is < Minimum Take It As Minimum Number

    print('Minimum Number Is : ', Minimum) # Display Min Elements

if __name__ == "__main__":
    main()