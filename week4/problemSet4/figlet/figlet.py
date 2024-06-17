import random
from pyfiglet import Figlet
import sys

figlet = Figlet()

# Define the available fonts
fonts = figlet.getFonts()

# If theres no command line arguments select a random font
if len(sys.argv) == 1:

    number_of_fonts = len(fonts)
    random_font = fonts[random.randrange(number_of_fonts)]

    # Set the font
    figlet.setFont(font = random_font)

    # Print the input received from user in a random font
    text = input("Input: ")
    print("Output: ", "\n", figlet.renderText(text))


# If the user specifies the font he wants to use
elif len(sys.argv) == 3:

    # Check if the font is inside the fonts list and the arguments are correct
    if sys.argv[2] not in fonts or sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    # Set the font if it is available
    figlet.setFont(font = sys.argv[2])

    # Print the input in the selected font
    text = input("Input: ")
    print("Output: ", "\n", figlet.renderText(text))

else:
    sys.exit("Invalid usage")
