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
