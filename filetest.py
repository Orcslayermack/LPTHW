text = "Hello Monica!"
file = "test.txt"
doc = open(file)

print "------------------------------------"
print "Here is the contents of", file
print "------------------------------------"

print doc.read()

print "------------------------------------"
print "Now let's write something into the file"
print "------------------------------------"

input = raw_input("> ")
print "we are going to add: \"", input, "\" to the file."
#doc.write(input)


doc.close()
