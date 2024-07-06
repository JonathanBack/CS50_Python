########### REGULAR EXPRESSIONS <-> regex

email = input("What's your email? ").strip()

#if "@" in email and "." in email:
#    print("Valid")
#else:
#    print("Invalid")

#username, domain = email.split("@")

#if (username) and domain.endswith(".edu"): # if username equals a string, not None or "", returns True AND endswith .edu
#    print("Valid")
#else:
#    print("Invalid")

    # re module
    # re.search(pattern, string, flags=0) pattern = search for something that repeats, string = what will be used to search for patterns

import re

#if re.search(".+@.+", email): # .+ = any character with 1 or more reps; ..* = any character and 0 or more characters
#    print("Valid")
#else:
#    print("Invalid")
    # pattern parameter can take multiple simbols:
    #   . = any character except anewline
    #   * = 0 or more repetitions
    #   + = 1 or more repetitions
    #   ? = 0 or 1 repetition
    #   {m} = m repetitions (specify the number of repetitions)
    #   {m,n} = m-n repetitions (specify the range of repetitions)
    #   ^ = matches the start of the string
    #   $ = matches the end of the string just before the newline at the end of the string
    #   [] = set of characters
    #   [^] = complementing the set

    # if you go from start state to except state the re.search will return True
    # start state = false, if re.search() finds the pattern youre looking for = true


    # matching start and end
if re.search(r"^.+@.+\.edu$", email): # backslash "\" and r in the begenining in regex means that this is a raw string and we're looking for .edu LITERALLY
    print("Valid")                    # use \ if you are looking for one of the special characters LITERALLY
else:
    print("Invalid")

    # sets of characters

if re.search(r"^[^@]+@[^@]+\.edu$", email): # [^@] means basically "." -> any character BUT "@"
     print("Valid")
else:
    print("Invalid")

    # this version is more restrictive, allows just a couple options, not EVERYTHING but "@"

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): # [a-zA-Z0-9_] specifies the ranges allowed AND the underscore "_"
     print("Valid")
else:
    print("Invalid")

    # Character classes
    #   \d = decimal digit      \D = not decimal digit      \s = whitespace characters      \S = not a whitespace character
    #   \w = word character, as well numbers and underscore         \W = not a word character
    #   A|B = eiter A or B      ( . . . ) = a group

if re.search(r"^\w+@\w+\.(edu|gov|net|com|org)$", email): #\w represents any word character, any alphanumerical character
     print("Valid")
else:
    print("Invalid")

    #   FLAGS
    #   re.IGNORECASE = case insensitive / re.MULTILINE = match different lines / re.DOTALL = dot recognize any carachter PLUS newlines

if re.search(r"^\w+@\w+\.(edu|gov|net|com|org)$", email, re.IGNORECASE): # re.IGNORECASE will do the same as changing the input
     print("Valid")
else:
    print("Invalid")

    # GROUPS
    # tolerate subdomains

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|gov|net|com|org)$", email, re.IGNORECASE): # (\w+\.)? = inside parenthesis is the submain, question mark means its optional (0 or 1 rep)
     print("Valid")
else:
    print("Invalid")

    # re.match(pattern, string, flag = 0)
    #   automatically starts matching the from the start of the string for you (same as using ^)
    # re.fullmatch(pattern, string, flag = 0)
    #   automatically statrs matching from the start to the end of the string (same as using ^ and $)


