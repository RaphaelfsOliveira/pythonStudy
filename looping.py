import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"


    
# test some code Looping WHILE#####################

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3

#code
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    print random_number
    if random_number == guess:
        print "You win!!"
        break
    guesses_left -= 1
else:
    print "You Lose!!"

    
# Looping FOR####################################

print "Counting..."

for i in range(20):
    print i
    

# work with dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print_this = key + " " + d[key]
    print print_this

# print index with the 

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index, item
