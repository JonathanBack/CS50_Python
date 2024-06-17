def main():
    greeting = input("Please, say any greeting :) ")
    ammount = value(greeting)
    print(f"${ammount}")

def value(greeting):
    greeting = greeting.title().strip()

    if greeting.startswith("Hello"):
        return 0
    elif greeting.startswith("H"):
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()



