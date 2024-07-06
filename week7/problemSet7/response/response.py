from validator_collection import validators, checkers, errors

def main():
    if check_email(input("What's your email address? ")):
        print("Valid")
    else:
        print("Invalid")

def check_email(text):
    is_email_address = checkers.is_email(text)
    return is_email_address

if __name__ == "__main__":
    main()
