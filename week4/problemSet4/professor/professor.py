import random as r


def main():

    level = get_level()

    questions = 10
    score = 0
    while questions > 0:

        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y

        wrong_answer = 0

        while True:
            try:
                print(x, "+", y, "=", end =" ")
                answer = input()
                if int(answer) == result:
                    score += 1
                    break

                else:
                    print("EEE")
                    wrong_answer += 1
                    if wrong_answer == 3:
                        print(x, "+", y, "=", result)
                        break


            except ValueError:
                pass

        questions -= 1

    print(score)

def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):

    try:
        if level not in [1, 2 ,3]:
            raise ValueError()

    except ValueError():
        print("Invalid level")
    if level == 1:
        number = r.randrange(10)
        return number

    elif level == 2:
        number = r.randrange(10, 100)
        return number
    else:
        number = r.randrange(100, 1000)
        return number


if __name__ == "__main__":
    main()
