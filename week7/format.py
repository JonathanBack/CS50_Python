    # format input the way we want
name = input("What's your name? ").strip()

#if "," in name:
#    last, first = name.split(", ")
#    name = f"{first} {last}"
#print(f"hello, {name}")

    # using re module
import re
    # if you use ( ) instead of only grouping you are capturing the values in this group

matches = re.search(r"^(.+), ?(.+)$", name) # you can have a return value of what exactly is a match

if matches:
    name = matches.group(2) + " " + matches.group(1) # parenthesis groups starts in 1, not 0
print(f"hello, {name}")

    # Walrus Operator -> :=
    # allows you to assign a value from right to the left and ask a bolean question about the assigned value

if matches := re.search(r"^(.+), ?(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
