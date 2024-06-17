'''
    # a little cryptic way of looking into a csv file and priting the values of each line
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",") # row is list with the values that once were separeted by commas
        print(f"{row[0]} is in {row[1]}") # printing the student name (row[0]) and their house (row[1])

 # more readable version of the same problem
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") # instead of creating a list you can assing each value to a variable
        print(f"{name} is in {house}") # printing the student name and their house.


 # sorting the students in alphabetical order
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}") # here i'm appending the whole sentence to the list

for student in sorted(students): # you are sorting by the whole sentence, and NOT by their exact name
    print(student)

 # creating an empty dictionary and filling it
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")

        #student = {}
        #student["name"] = name
        #student["house"] = house

        student = {"name": name, "house": house} # create a dictionary and the keys: values
        students.append(student) # creates a list of dictionaries


def get_name(student):
    return student["name"] # return the key name in the dictionary
def get_house(student):
    return student["house"]


for student in sorted(students, key=get_name, reverse = True): # you can pass a function as a parameter for another function
    # get_name wil be called be sorted(), return the strings defined in the function and will be used to define how to sort the strings
    print(f"{student['name']} is in {student['house']}")

 # tighten the code
 # Lambda function (anonymous function)
 # lambda parameter: return value
 # Example -> lambda student: student["house"]
 # lambda will recieve the student as a parameter and will return the value for the key "house" in that dictionary
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house} # create a dictionary and the keys: values
        students.append(student) # creates a list of dictionaries

for student in sorted(students, key=lambda student: student["name"]): # lambda is equivalent to the get_name() writen above, takes a paramenter: lambda parameter: return
    print(f"{student['name']} is in {student['house']}")

 # students2.csv

students = []

with open("students2.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",") # this line returns a ValueError because of Harrys adress (too many values to unpack)
        student = {"name": name, "home": home}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

 # using CSV library/module

import csv

students = []

with open("students2.csv") as file:
    reader = csv.reader(file) # reader(file) will deal with the value between "..." and return a list with the values
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}, version one")
'''
    # storing the name of the columns in the csv itself
    # using csv DictReader
    # adding a new column to the csv file will break the code above, the code bellow deals just fine with it and any other future changes
    # due to the dictionary reader, the columns names specified in the csv file allow us to know the keys for the dict and code with them
students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file) # DictReader(file) will return individual dictionaries and the NAME for each column (the keys for the dict)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]}) # this way makes the code more robust to changes in the csv value!

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
