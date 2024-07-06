from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    date_in_minutes = get_diff(input("Date of Birth: "))
    sentence = get_sentence(date_in_minutes)
    print(f"{sentence} minutes")

def get_diff(birthday):

    # use date.today() class method to get todays date
    today = date.today()
    try:
        # transform string of a date in iso format to a date object
        date_of_birth = date.fromisoformat(birthday) #(YYYY-MM-DD)
        # if the input is not in ISOFORMAT -> sys.exit
    except ValueError:
        sys.exit("Invalid date")

        # use operator.sub (operator overloading) to get the difference from the two times, return the diff in DAYS
    diff = today - date_of_birth
        # transform the diff from days to total_seconds and then divide by 60 to get the difference in minutes
    minutes = int(diff.total_seconds() / 60)
    return minutes

def get_sentence(number):
        # use inflect library and number_to_words module to convert the number to a sentence, removing and from the sentence as well
    sentence = p.number_to_words(number, andword="").capitalize()

    return sentence


if __name__ == "__main__":
    main()
