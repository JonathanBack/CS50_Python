import random as r

while True:
    try:
        level = int(input("Level: "))
        number = r.randint(1, level)
        break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass


