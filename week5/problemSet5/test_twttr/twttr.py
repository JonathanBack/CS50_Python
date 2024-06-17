
def main():

    word = input("Input: ")
    abv_word = shorten(word)

    print("Output:", abv_word)

def shorten(word):

    abreviation = ""
    for letter in word:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            abreviation += letter
    return abreviation


if __name__ == "__main__":
    main()

