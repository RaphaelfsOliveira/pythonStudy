class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()


# Class definition
class Animal(object):
    """Makes cute animals."""
    # initializing instance objects with method init
    def __init__(self, name, age, is_hugry):
        self.name = name
        self.age = age
        self.is_hungry = is_hugry


#create objects
zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

##class
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #create method 
    def description(self):
        print self.name
        print self.age

hippo = Animal("Hathi", 42)

print hippo.description()


#example of shopping cart in real program 
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."
            
            
my_cart = ShoppingCart("Raphael")
print my_cart.customer_name

my_cart.add_item("Moto X2", 500)
my_cart.add_item("Moto Z Play", 1500)
my_cart.add_item("Moto X2", 500)

print my_cart.items_in_cart.items()
print my_cart.items_in_cart.keys()
print my_cart.items_in_cart.values()

my_cart.remove_item("Lenovo Vibe")
my_cart.remove_item("Moto Z Play")
            
