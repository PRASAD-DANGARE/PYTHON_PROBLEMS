import re

first_multiple_input = input().rstrip().split() # rstrip removes all the trailing characters & removes all the specified characters from right side of the string
                                                #  split a string into a list of strings 

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

#n, m = map(int, first_multiple_input)

matrix = []

for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix = list(zip(*matrix)) # get the string into list of string and zip them (combine) and (*) get one by one character separately

#print(matrix)

decoded = ''

for i in matrix:
    decoded += ''.join(i)

decoded = re.sub(r'\b[^a-zA-Z0-9]+\b',r' ', decoded) # re.sub() is used to replace substrings in strings, \b represents the backspace character
print(decoded) # display the string , \r represent Carriage Return 