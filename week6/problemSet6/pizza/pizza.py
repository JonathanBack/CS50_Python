import sys
import csv
from tabulate import tabulate

    # check the ammount of command line arguments (must be equal to 2)
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

    # check if the extension is correct (must be .csv)
file_name, extension = sys.argv[1].split(".")
if extension != "csv":
    sys.exit("Not a CSV file")

    # try to open a csv file, otherwise sys.exit()
try:
    table = []
    with open(sys.argv[1]) as file: # open the command line argument with the name of the file (ideally .csv)
        reader = csv.DictReader(file)   # reads the csv file as a dictionary
        for row in reader:      # reads each line of the file as a dictionary
            table.append(row)   # append the "row" dictionary to an empty list


except FileNotFoundError:
    sys.exit("File does not exist")     # sys.exit() if the csv file was not found

print(tabulate(table, headers="keys", tablefmt = "grid"))  # print the list of dictionaries with their keys as firstrow and with ASCII art

