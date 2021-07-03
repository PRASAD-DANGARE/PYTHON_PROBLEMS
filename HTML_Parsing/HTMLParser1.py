'''
Class Name       :  MyHTMLParser
Description      :  Demonstration Of HTML Parser Application
Function Date    :  03 July 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

#============================
#
# IMPORTS
#
#============================

from html.parser import HTMLParser # HTMLParse Parsing Text Files Formatted In HTML

# Create A subclass And Override The Handle Methods

#============================
#
# HTMLParser Class
#
#============================

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):  # tag argument is the name of the tag converted to lowercase, 
                                            # attrs argument is a list of(name,value)pairs containing the attributes found inside the tag’s
        print("Encountered A Start Tag  : ", tag)

    def handle_endtag(self, tag):
        print("Encountered An End Tag   : ", tag)

    def handle_data(self, data):
        print("Encountered Some Data    : ", data)

    def handle_startendtag(self, tag, attrs):
        print ("Found An Empty Tag       : ", tag)

# Instantiate The Parser And Fed It Some HTML

parser = MyHTMLParser()
parser.feed('<html><br/><head><title>HTML Parser - I</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

#============================
#
# Entry Point
#
#============================

def main():

    obj1 = MyHTMLParser()

#============================
#
# Code Starter
#
#============================

if __name__ == "__main__":
    main()

'''

Output : 

Encountered A Start Tag  :  html
Found An Empty Tag       :  br
Encountered A Start Tag  :  head
Encountered A Start Tag  :  title
Encountered Some Data    :  HTML Parser - I
Encountered An End Tag   :  title
Encountered An End Tag   :  head
Encountered A Start Tag  :  body
Encountered A Start Tag  :  h1
Encountered Some Data    :  Parse me!      
Encountered An End Tag   :  h1
Encountered An End Tag   :  body
Encountered An End Tag   :  html

'''

# HTML Parser Application, HTMLParser That Uses The HTMLParser Class To Print Out 
# Start tags, end tags, And Data As They Are Encountered.

# or An HTMLParser instance is fed HTML data and calls handler methods when 
# start tags, end tags, text, comments, and other markup elements are encountered.

# pip install HTMLParser
