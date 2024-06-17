def main():
    name = input("What's your name? ")
    '''
    hello(name)
    hello() #default is world
    '''
    print(hello(name))


    # OLD hello() function
    # when a function like hello() does not return anything, you can say it has the "Side effect" of printing something
    # or doing something else visualy <- IT IS HARD TO TEST, having a return value makes it testable
'''
def hello(to="world"):
    print("hello,", to)
'''

# NEW IMPROVED hello( ) function

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
