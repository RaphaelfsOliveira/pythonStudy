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

# adicionando dados a um vetor
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("chinello")
suitcase.append("Toalha")
suitcase.append("Touca")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase
