'''
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that
 a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then
outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate
that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

'''




def main():

    #recieve a fraction x/y and split it into two variables
    fraction = input("Fraction: ")

    percentage = convert(fraction)

    output = gauge(percentage)
    print(output)

def convert(fraction):
    try:
            x, y = fraction.split(sep="/")
            x, y = int(x), int(y)

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            else:
                percentage = round((x / y * 100)) #fuel in %
                return percentage

    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)+"%"




if __name__ == "__main__":
    main()
