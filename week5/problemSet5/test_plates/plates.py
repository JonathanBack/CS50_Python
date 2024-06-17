'''
Among the requirements, though, are:

    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable vanity
    plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or
Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein
is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement
additional functions for is_valid to call (e.g., one function per requirement).
'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(string):

    #may contain max of 6 characters (letters or numbers) and min of 2 characters
    if len(string) < 2 or len(string) > 6:
        return False
    #check if the plate is entirely alphabetical
    if string.isalpha():
        return True
    #if contains numbers, must start with at least 2 letters
    elif string.isalnum() and string[0:2].isalpha():
        #check the string for numbers
        for character in string:
            if character.isnumeric():
                #if the character is numeric, find the index of the first number
                position = string.index(character)

                #check if the string is entirely numeric from that index beyond and if the first number is != 0
                if string[position:].isnumeric() and character != "0":
                    print(string[position:])
                    return True
                else:
                    return False
    else:
        return False
if __name__ == "__main__":
    main()
