
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
    
#print random_row(board)
#print random_col(board)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col

for turn in range(4):
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    print "Turn, " + str(turn)
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col  > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    print_board(board)
    print "Turn", turn + 1
    if turn == 3:
    print "Game Over"
