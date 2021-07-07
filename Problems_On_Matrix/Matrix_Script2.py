'''

Function Name    :  None
Description      :  Accept Row, Column And Elements From User And Decode Them & Display
Function Date    :  07 July 2021
Function Author  :  Prasad Dangare
Input            :  Str, Special Simbol
Output           :  Str, Special Simbol

'''

import re

First_Multiple_Input = input().rstrip().split()

Row = int(First_Multiple_Input[0])
Col = int(First_Multiple_Input[1])

# Row, Col = map(int, First_Multiple_Input)

matrix = []

for i in range(Row):
    matrix_item = input()
    matrix.append(matrix_item)

matrix = list(zip(*matrix))
#print(matrix)

decoded = ''

for i in matrix:
    decoded += ''.join(i)

decoded = re.sub(r'\b[^a-zA-Z0-9]+\b',r' ', decoded)
print(decoded)

'''

matrix script is a N(Row) X M(Col) grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

eg : 

T   s   i
h   %   x
i
s   M
$   a
#   t   %
i   r   !

To decode the script, read each column and select only the alphanumeric characters and connect them,
reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then replaces them with a single space ''

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input :
            7   3
            T s i
            h % x
            i   #
            s M
            $ a
            # t %
            i r !

decoded script is : This$#is% Matrix#  %! , replaces the symbols or spaces between two alphanumeric characters with a single space

final Output : This is Matrix#  %!

'''
