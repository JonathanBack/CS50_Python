    # WRITING DATA IN A CSV FILE
    # USING csv.writer()
'''
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("writeStudents.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home]) # <- if the string home has a comma for gramatical pourpuse, it will automatically put the string in double quotes in the csv file: "string"
'''

    # USING csv.DictWriter()
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("writeStudents.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"]) # fieldnames = specifies the order of the columns to be writen in the dict
    writer.writerow({"home": home, "name": name})
