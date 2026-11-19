f = open("file.txt")

# lines = f.readlines() #Reads all the lines in a list. type is list

# line1 = f.readline() #Reads only one line. 
# print(line1, type(line1)) #Prints only one line. type is str

# line2 = f.readline() #Reads the next line. 
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline() #goes to the next line

f.close()