import sys
import os
from PIL import Image, ImageOps

    # check if the user infomrs the input and output name
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

    # check if the extension is correct (must be .png, .jpeg or .jpg)
input_name, input_extension = os.path.splitext(sys.argv[1])
if input_extension.lower() not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")

output_name, output_extension = os.path.splitext(sys.argv[2])
if output_extension.lower() not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")

    # compare the extensions to see if they are the same
if output_extension.lower() != input_extension.lower():
    sys.exit("Input and output have different extensions")

    # open the shirt png that will be used to overlay other images
shirt = Image.open("shirt.png")
size = shirt.size # (600, 600) tuple of the size of shirt.png

try:
    with Image.open(sys.argv[1]) as im: # -> Image
        photo = ImageOps.fit(im, size) # resize the img to fit shirt.png
        photo.paste(shirt, mask = shirt) # overlay the photo with shirt
        photo.save(sys.argv[2]) # save with the output gave on command line

except FileNotFoundError:
     sys.exit("Input does not exist")











