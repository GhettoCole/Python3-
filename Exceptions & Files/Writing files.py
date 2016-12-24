# To write files, use the write method, which writes a string to the file

file = open("new.txt", "w")  # The 'w' mode writes a file if it doesn't already exist
file.write("I want to be a programmer, hacker and a full stack web developer\n"
           "Plus I want to hack the government, not for malicious purposes but to expose of the truth!")
file.close()

file = open("new.txt", "r")
print(file.read())
file.close()

# When a file is opened in write mode, the file's existing content is deleted
file = open("new.txt", "r")
print("\nReading initial contents")
print(file.read())
print("\nFINISHED")

file = open("new.txt", "w")
file.write("Programming is magical, its like writing poetry and revealing what is inside your heart\n"
           "Not just for fun but for the world to see your inner abilities")
file.close()

file = open("new.txt", "r")
print("\nReading new contents\n")
print(file.read())
print("\nDONE")
file.close()

# The write method returns the number of bytes written to a file, if successful
msg = "Ghettocole is fucken awesome"
file = open("msg.txt", "w")
_bytes = file.write(msg)
print(_bytes)
file.close()
