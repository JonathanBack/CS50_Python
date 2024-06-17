import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    file_name, extension = sys.argv[1].split(".")
    if extension != "py":
        sys.exit("Not a Python file")
except ValueError:
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        lines_of_code = 0
        for line in file:
            if not line.lstrip().startswith('#') and len(line.lstrip()) != 0:
                lines_of_code += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(lines_of_code)

