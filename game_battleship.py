
### como eu fiz o game... 
board = []

def create(lst):
    
    ls = []
    
    for i in range(5):
        lst.append("O")
        ls.append(lst)
    
    #return lst
    return ls

"""    
def create_sub(lst):
    
    ls = []
    
    for i in range(0,5):
        ls.append(lst)

    return ls
"""

print create(board)

print

for i in range(5):
    print board

    
###como o exercício manda fazer 

board=[]

for x in range(0,5):
    r=['O']*5
    board.append(r)
    
def print_board(board):
    for row in board:
        print " ".join(row)

print print_board(board)

#add function random########################
from random import randint # import random module

def random_row(board):
    return randint(0, len(board) - 1)
    
def random_col(board):
    return randint(0, len(board) - 1)
    
print random_row(board)
print random_col(board)
