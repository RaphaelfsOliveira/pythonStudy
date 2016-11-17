doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1,12) if (x**2) % 2 == 0]

print even_squares

####

cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]

print cubes_by_four

##

l = [i ** 2 for i in range(1, 11)]
#print [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]


###omitting indices

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

# exemple

my_list = range(1, 11) # List of numbers 1 - 10

# print only odd numbers
print my_list[::2]

#create list of 1 to 21 incluse
to_21 = [x for x in range(1,22)]

#only odd numbers
odds = to_21[::2]

middle_third = to_21[7:14:]

###reverse list

my_list = range(1, 11)

# reverse my_list
backwards = my_list[::-1]

print my_list
print
print backwards


#copy list

to_one_hundred = range(101)

#by ten
backwards_by_tens = to_one_hundred[::10]

print backwards_by_tens
