def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        #print(i, range(n), end =" ") #print is a good way to display whats happening on the code to debug it
        print("#" * (i + 1))

if __name__ == "__main__":
    main()
