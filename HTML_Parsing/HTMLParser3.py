'''
Class Name       :  MyHTMLParser
Description      :  HTML Parser Application To Accept Input From User And Check The Type Of Comment And Display The Data
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
  
    def handle_comment(self, data):
      
        Comment_lines = len(data.split('\n'))

        if Comment_lines > 1:
            print(">>> Multi-line Comment")
        
        else:
            print(">>> Single-line Comment")

        if data.strip():
            print(data)

    def handle_data(self, data):

        if data.strip():
            print(">>> Data")
            print(data)

#============================
#
# Entry Point
#
#============================

def main():
      
    html = ""       
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'
    
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

#============================
#
# Code Starter
#
#============================

if __name__ == "__main__":
    main()

    

'''
Input : 4                                           
        <!--[if IE 9]>IE9-specific content         
        <![endif]-->                       
        <div>Welcome to Development</div>   
        <!--[if IE 9]>specific content<![endif]-->

Output :
        >>> Multi-line Comment
        [if IE 9]>IE9-specific content     
        <![endif]
        >>> Data
        Welcome to Development
        >>> Single-line Comment
        [if IE 9]>specific content<![endif]

'''