# This next line assigns a string with the number 10 at %d to the var x
x = "there are %d types of people." % 10

# This assigns the string "binary" to the var binary
binary = "binary"
# Same thing here
do_not = "don't"

# Same thing here but with two vars to the string
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the two strings
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
