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


## adicionando itens com preço em um "menu"

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Hamburguer'] = 32.90
print menu['Hamburguer']

menu['Spam'] = 2.58

print "There are " + str(len(menu)) + " items on the menu."
print menu


# vetor com varios registros e seus valores

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# deletando registros do vetor
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

# mudando valores dos registros
zoo_animals['Rockhopper Penguin'] = 'Americas'

print zoo_animals


# removendo itens da lista

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove('dagger')

print backpack


########

# lista inventario
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# adicionando uma chave que contem uma lista
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# arrumando a lista sort por ordem alfabetica
inventory['pouch'].sort() 

# adicionando a chave pocket a lista inventario
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# arrumando a lista backpack por ordem alfabetica
inventory['backpack'].sort()

# removendo um registro da chave inventário
inventory['backpack'].remove('dagger')

# adicionando mais 50 de ouro a chave gold
inventory['gold'] += 50
