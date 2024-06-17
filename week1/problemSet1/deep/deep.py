##########
#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe
#and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
#Otherwise output No.
##########
question = input("Answer the Great Question of Life, the Universe and Everything. ").strip().title()

match question:
    case "42" | "Forty-Two" | "Forty Two":
        print("Yes")
    case _:
        print("No")
