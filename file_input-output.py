# Open the file
read_file = open("text.txt", "w")
read_file = open("text.txt", "r")

#open the file for writing
write_file = open("text.txt", "w")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

#always close the file
write_file.close()

#print read file
print read_file.read()

#always close the file
read_file.close()

########################################
#method that close the file auto
with open("text.txt","w") as my_file:
    my_file.write("Jack and Jill")

    
######close file    
with open("text.txt","w") as my_file:
    my_file.write("Jack and Jill")
    
if not my_file.closed:
    my_file.close()
    
print my_file.closed
