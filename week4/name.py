import sys

#sys.argv: a list of everything you write on the terminal
#Terminal: python name.py Jonathan
#[0] = name.py // [1] = Jonathan

#print("hello, my name is", sys.argv[1])
#if the user does not type their name -> IndexError: list index out of range

#Check the errors // sys.exit quits the code on the spot
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")

#Print name tags
#print("hello, my name is", sys.argv[1])

#Print multiple name tags
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
