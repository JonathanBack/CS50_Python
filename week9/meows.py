    # CONSTANTS
'''
MEOWS = 3

for _ in range(MEOWS):
    print("meow")


class Cat:
    MEOWS = 3
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()
'''



    # USING MYPY AND TYPE HINTS
    # execute like pytest or python3 -> mypy file.py
        # examples of messages from mypy:
            # Success: no issues found in 1 source file
            # meows.py:28: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
            # Found 1 error in 1 file (checked 1 source file)

    # def function(variable: type) -> return hint
    
def meow(n: int) -> str:
    '''
    for _ in range(n):
        print("meow")
    '''

    # docstring documentation format
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """

    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number) # if meow() has no return value, it returns None
print(meows, end="") # prints None if theres no return value

