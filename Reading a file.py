#f = open("HARRY.TXT", "rt")       #made a text file "harry,txt",read text mode on
#content = f.read()         #printing of all content in file
#print(content)
#f.close()
#print(f.readline())          #reading line by line
#print(f.readline())
#print(f.readlines())     #making list from the file lines
#f = open("HARRY.TXT", "w")       # in write mode
#f.write("vaishu is cute")     #rewrites the file,removes the older data with inputted data
f = open("HARRY.TXT", "a")
f.write("vaishu")
f.close()



