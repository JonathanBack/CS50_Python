'''
In a file called camel.py, implement a program that prompts the user for the name of a variable
in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
'''

variable = input("Write a variable in camelCase: ")

for letter in variable:
    if letter.isupper():
       print("_" + letter.lower(), end="")
    else:
        print(letter, end="")
print()
