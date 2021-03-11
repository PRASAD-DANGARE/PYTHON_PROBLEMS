'''

Class Name    : BookStore
Function Name : Display()
Description   : Accept Book Name And Author From User & Display It 
Author        : Prasad Vijaykumar Dangare
Date          : 10 Mar 2021

'''

class BookStore:

    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author

    def Display(self):
        return self.Name, self.Author
    
def main():

    x = (input("Enter Book Name : "))
    y = (input("Enter Book Author : "))

    obj1 = BookStore(x, y)

    Ret = obj1.Display()
    print("Book Name is {}, Author is {} ".format(x, y, Ret))
    
if __name__ == "__main__":
    main()

'''
class BookStore:

    NoOfBooks = 0

    def __init__(self, name, auther):
        self.name = name
        self.author = auther
        BookStore.NoOfBooks += 1

    def Display(self):
        print("book is:{} \n auther is : {} \n no of books : {}".format(self.name, self.author, self.NoOfBooks))


def main():

    Obj1 = BookStore('LinuxSystemProgramming', 'RobertLove')
    Obj1.Display()  

    Obj2 = BookStore('C Programming', 'Dennis Ritchie')
    Obj2.Display()
    
    Obj3 = BookStore('C Programming', 'Dennis Ritchie')
    Obj3.Display()

if __name__=="__main__":
    main()

'''
    