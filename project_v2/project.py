import argparse
import sys
import re

if len(sys.argv) < 3:
    sys.exit("usage: project.py [-h] [--height HEIGHT] [--mass MASS] [-s SYSTEM]")

parser = argparse.ArgumentParser(
    prog="project.py",
    description="Calculates Body Mass Index with given height and mass",
    epilog=""
)

parser.add_argument("--height", help="height in Meters or Feet\'Inches\"", type=str)
parser.add_argument("--mass", help="Mass in Kilograms (kg) or pounds(lb)", type=float)
parser.add_argument("-s", "--system", help="Unit system of mass and Height. Metric System or Imperial System", type=str)
args = parser.parse_args()


height = args.height
mass = args.mass
unit_system = args.system.lower()


print(height, mass, unit_system)


def main():
    meters = check_height(height, unit_system)
    kg = check_mass(mass, unit_system)
    bmi = calculate_bmi(meters, kg)
    print(bmi)

def calculate_bmi(height_in_meters, mass_in_kg):
    """
    calcultes the bmi with given height and mass and returns the bmi
    bmi = kg/m**2
    """

    bmi = (mass_in_kg/height_in_meters**2)
    return bmi

def check_height(height, unit_system):
    """
    checks the unit system, if it is metric returns the float of the units
    if it is imperial, converts the units and then return the float of them
    1 inch = 0.0254 meters
    1 feet = 12 inches
    """
    if unit_system == "metric":
        meters = float(height)
        return meters

    if unit_system == "imperial":
        unit = re.search(r"^(\d)'(\d*)?\"?$", height)

        if unit == None:
            
            sys.exit("Invalid height. Please use the format: Ft'Inches\", e.g 6\'11\"")

        if unit.group(2) == None:
            inches = 0

        else:
            inches = float(unit.group(2))

        feet = float(unit.group(1))

        meters = round(((feet * 12) + inches) * 0.0254, 2)
        return meters

def check_mass(mass, unit_system):
    if unit_system == "metric":
        kg = float(mass)
        return kg
    if unit_system == "imperial":
        pounds = float(mass)
        kg = round(pounds/2.205, 1)
        return kg

if __name__ == "__main__":
    main()
