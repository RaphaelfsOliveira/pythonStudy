####functional programming
"""
One of the more powerful aspects of Python
is that it allows for a style of programming 
called functional programming, which means that 
you're allowed to pass functions around just as 
if they were variables or values. Sometimes we 
take this for granted, but not all languages allow this!
"""

my_list = range(16)

print filter(lambda x: x % 3 == 0, my_list)

####
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda i: i == "Python", languages)

####

squares = [x**2 for x in range(1,11)]
print filter(lambda x: x > 30 and x <= 70, squares)

#####

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
print message
