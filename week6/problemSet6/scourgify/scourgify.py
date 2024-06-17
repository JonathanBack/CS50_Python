import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    students = []
    with open(sys.argv[1]) as file: # open the command line argument with the name of the file (ideally .csv)
        reader = csv.DictReader(file)   # reads the csv file as a dictionary
        for row in reader:      # reads each line of the file as a dictionary
            students.append(row)   # append the "row" dictionary to an empty list


except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])     # sys.exit() if the csv file was not found


    # creates a new file with the third command line argument as its name

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"]) # fieldnames = specifies the order of the columns to be writen in the dict
    writer.writeheader()    # writes the header (first row) with the fieldnames in the new file

    for student in students:

        last, first = student['name'].split(", ")   # splits the name column into two new columns
        house = student['house']
        writer.writerow({"first": first, "last": last, "house": house}) # writes the rows with the new columns
