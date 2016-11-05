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
