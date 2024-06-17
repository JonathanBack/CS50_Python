'''
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
E = m * pow(c, 2) C == 300000000
'''
def main():
    mass = int(input('--->'))
    energy = einstein(mass)
    print(energy)

def einstein(mass):
    C = 300000000
    return(mass * pow(C,2))
main()
