'''
Class Name       :  MyHTMLParser
Description      :  HTML Parser Application To Accept Input From User And Display It
Function Date    :  03 July 2021
Function Author  :  Prasad Dangare
Input            :  Int,str
Output           :  str

'''

#============================
#
# IMPORTS
#
#============================

from html.parser import HTMLParser

#============================
#
# MyHTMLParser Class
#
#============================

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):        
        print ('Start :', tag)
        
        for elements in attrs:
            print ('->', elements[0], '>', elements[1])
            
    def handle_endtag(self, tag):
        print ('End   :', tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        
        for elements in attrs:
            print ('->', elements[0], '>', elements[1])

#============================
#
# Entry Point
#
#============================

def main():

    iNo = int(input())
    HTMLParsing = MyHTMLParser()
    str = ""

    for i in range(iNo):
        str += input().strip()

    HTMLParsing.feed(str)

    #HTMLParsing = MyHTMLParser()
    #HTMLParsing.feed(''.join([input().strip() for str in range(int(input()))]))

#============================
#
# Code Starter
#
#============================

if __name__ == "__main__":
    main()



'''
Input : 2
        <html><head><title>HTML Parser - I</title></head>  
        <body data-modal-target class='1'><h1>BackendDevelopment</h1><br /></body></html>

Output :

Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html

'''