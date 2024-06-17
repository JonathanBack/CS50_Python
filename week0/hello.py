#Ask user for their name, remove whitespaces from str and capitalize
name = input("What's your name? ").strip().title()

#Split user's name into first and last name
first, last = name.split(" ")

#Say hello to user
print(f"Hello, {first}", end="")
print(". How are you doing?")


