'''
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that
file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead,
which is a common default.
'''
#recieve the file
question = input("Give the name of a file: ").lower().strip()

extension  = question.rsplit(sep=".", maxsplit=1)
reverse = extension[::-1]

if reverse[0] in ("gif", "png"):
    print('image/'+reverse[0])
elif reverse[0] in ("jpg", "jpeg"):
    print('image/jpeg')
elif reverse[0] in ("pdf", "zip"):
    print('application/'+reverse[0])
elif reverse[0] in ("txt"):
    print('text/plain')
else:
    print("application/octet-stream")
