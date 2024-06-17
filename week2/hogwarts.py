'''
students = ["Hermione", "Harry", "Ron"]


#1
for student in students:
    print(student)

#2 range and len
for i in range(len(students)):
    print(i + 1, students[i])
'''
#3 dict -> associate lists
'''
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


#dict ----> KEY: VALUE
#if you print(dict[KEY]) you will return the VALUE
#dict = {"KEY": "VALUE"}
#print(dict["KEY"])
#terminal: VALUE

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")
    #print(students["Hermione"])
'''
#4 dict with more info associated (name, house, patronus) list of dicts
#each dict has 3 KEYS, (name, house, patronus)
#dict is just a colection of values associated with keys
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")
