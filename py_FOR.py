n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
         print x[i]
    
print_list(n)

####

#Method 1 - for item in list:

#Method 1 is useful to loop through the list, 
#but it's not possible to modify the list this way.

for item in list:
    print item

#Method 2 - iterate through indexes:

#Method 2 uses indexes to loop through the list, 
#making it possible to also modify the list if needed. 
#Since we aren't modifying the list, feel free to use either one on this lesson!

for i in range(len(list)):
    print list[i]



