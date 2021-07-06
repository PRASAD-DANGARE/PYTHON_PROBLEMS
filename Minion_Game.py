'''

Function Name    :  Minion_Game
Description      :  Accept String In Upper Case From User, Both The Players Create Substring From Input String As
                    Kevin - consonants, Stuart - Voewls And Based On That They Get There Score And How's Score Is High They Win This Game

Function Date    :  06 July 2021
Function Author  :  Prasad Dangare
Input            :  Str
Output           :  Str

'''

#=======================
#
# Minion Game Operation
#
#=======================


def Minion_Game(Input_string):
    
    if Input_string >= 'a' and Input_string <= 'z':
        exit("Invalid Input! | Note : Please Give Input In Upper Case")

    if Input_string.isalpha() is False:
        exit("Invalid Input! | Note : Please Give Input In String")

    KEVIN = 0
    STUART = 0

    SCORE = len(Input_string)

    for value in range(SCORE):

        if Input_string[value] == 'A' or  Input_string[value] == 'E' or Input_string[value] == 'I' or Input_string[value] == 'O' or Input_string[value] == "U":
            KEVIN += SCORE - value

        else:
            STUART += SCORE - value

    if STUART > KEVIN:
        print("Stuart", STUART)

    elif STUART < KEVIN:
        print("Kevin", KEVIN)

    else:
        print("Draw")


#====================
#
# Entry Point 
#
#====================

def main():
    
    Str_Input = str(input().strip())
    Minion_Game(Str_Input)

    '''
    str_name = input()
    Minion_Game(str_name)
    '''

#====================
#
# Code Starter
#
#====================


if __name__ == "__main__":
    main()

'''

Game Rules : 

2 Players Kevin, Stuart
Both players are given the same string
Both players have to make substrings using the letters of the string
Stuart has to make words starting with consonants
Kevin has to make words starting with vowels
The game ends when both players have made all possible substrings

Scoring :

A player gets +1 point for each occurrence of the substring in the string
eg :    BANANA
        Kevin's vowel beginning word = ANA
        Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points

Input : BANANA
Output : Stuart 12

Input : BAANANAS
Output : Kevin 19

Input : BANANANAAAS
Output : Draw

'''
