def main():
    #removing the int() function
    #x = int(input("What's x? "))
    x = input("What's x? ")
    print("x squared is", square(x))

#BROKE square FUNCTION changing * to +
def square(n):
    return n * n
    #return n + n

if __name__ == "__main__":
    main()

