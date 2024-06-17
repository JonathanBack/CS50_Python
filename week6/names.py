# appending names to an empty list
'''
names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

for name in sorted(names):
    print(f"hello, {name}")


 # saving the input to a file
name = input("What's your name? ")


file = open("names.txt", "a") # open a file (.txt), and write ("w") and RECREATE the file everytime you open it, append "a" adds each time you run it
file.write(f"{name}\n")
file.close() # you dont need to use .close() if you do the code bellow

 # USING WITH ... AS ... :
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
'''
 # READING FILES
with open("names.txt", "r") as file: # "r" means read the file
    lines = file.readlines() # returns all the lines from the file as a LIST

for line in lines:
    print("hello,", line.rstrip()) # .rstrip() or end = "" to remove empty lines from the print function

 # Shorter way, but you wont have the chance to sort the lines because you printing them just after being read
with open("names.txt", "r") as file:
    for line in file:                   # you dont need to create a new object, for will automatically iterate through each line
        print("hello,", line.rstrip())

 # sorting the names alphabetically and creating an empty list, so you can later manipulate the itens on the list however you want ".upper()", etc
names = []

with open("names.txt") as file: # no need to specify "r", open() reads a file by default
    for line in file:
        names.append(line.rstrip()) # .rstrip() removes empty lines at the end of each line

for name in sorted(names):
    print(f"hello, {name}")

 # you can sort the file itself

with open("names.txt") as file:
    for line in sorted(file, reverse = True): # reverse parameter will sort in reverse order when = True
        print("hello,", line.rstrip())

