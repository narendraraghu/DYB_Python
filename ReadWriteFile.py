# In java File file = FileUtils.getFile("/tmp/foo.txt");


# read line by line
f = open("/Users/narendra.raghuwanshi/Desktop/pascal.txt","r")
for line in f:
  print(line)
f.close()

# read the entire file in memory
f = open("/Users/narendra.raghuwanshi/Desktop/pascal.txt","r")
contents = f.read()
print(contents)
f.close()

# write to a file
f = open("/Users/narendra.raghuwanshi/Desktop/pascal.txt","r+") # open for both read and write
f.write("This is a test from Python")
contents = f.read()
print(contents) # will print "This is a test"


