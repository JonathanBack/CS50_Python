'''
x = int(input("What's x? "))
print(f"x is {x}")
'''
#if someone input a str with alphabetical characters:
    #ValueError: invalid literal for int() with base 10: 'dog'
    #literal = (input 'dog') and it is invalid for int( ) function

'''

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

#you try a conditional an if it fails with certain errors, like ValueError, the except function will proceed to execute what you determine bellow


#best pratices: Only write in between try and except the minimium necessary, for example: the print function above could be outside of try and except
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

#NameError: name 'x' is not defined -> int() can't recieve a string if you input "cat", and then line 26 breaks.


#How to fix:
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

#How to reprompt the user until he inputs smth that works

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")

#Defining a function
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? ")) #you can shorten the code above, remove else: break and just return the input if it yes correct (under try)
        except ValueError:
            print("x is not an integer")

main()

#Pass:
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass #if you don't want to further deal with the error you can do this

main()
'''
#add a parameter to get_int(), you can reuse the get_int function by just changing the prompt parameter
def main():
    x = get_int("What's y? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass #if you don't want to further deal with the error you can do this

main()
