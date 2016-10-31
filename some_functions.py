def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# Print out the types of an integer, a float,
# and a string on separate lines below.

print type(42)

print type(4.2)

print type('Spam')

print type(True)

################## OPERAÇÕES COM VETORES
# adicionando dados a um vetor
suitcase = [] 
suitcase.append("sunglasses") # adicionando um dado ao final do vetor

# Your code here!
suitcase.append("chinello")
suitcase.append("Toalha")
suitcase.append("Touca")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

# vetor animais
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
# procurando um animal na lista
duck_index = animals.index("duck") # Use index() to find "duck"

# inserindo um animal no index do vetor que voce quiser
animals.insert(2,"cobra")

print duck_index 
print animals # Observe what prints after the insert operation


start_list = [5, 3, 1, 2, 4]
square_list = []

# fazendo a operação e salvando em outro vetor
for number in start_list:
    square_list.append(number**2)

print square_list

# organizando a lista do menor para o maior funciona com string tambem
square_list.sort()

print square_list
