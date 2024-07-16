import argparse
import re
import sys
import csv
import os
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(
        prog="project.py",
        description="Calculates Body Mass Index with given height and mass",
        epilog="Please take care with the Height when using the imperial system, it must be denoted as 'X feet Y inches', with quotes surrounding the height (e.g '5 feet 11 inches'). Otherwise the program will not run."
    )

    parser.add_argument("--height", help="Height in the format 'X feet Y inches' for imperial or 'X.Y' for metric", type=str, required=True)
    parser.add_argument("--mass", help="Mass in Kilograms (kg) or Pounds (lb). No need to inform the unit.", type=str, required=True)
    parser.add_argument("-s", "--system", help="Unit system of mass and height. Metric or Imperial", type=str, choices=['metric', 'imperial'], required=True)
    args = parser.parse_args()

    HEIGHT = args.height
    MASS = args.mass
    UNIT_SYSTEM = args.system.lower()

    print(f"Height: {HEIGHT}, Mass: {MASS}, Unit System: {UNIT_SYSTEM}")

    try:
        meters = check_height(HEIGHT, UNIT_SYSTEM)
        kg = check_mass(MASS, UNIT_SYSTEM)
        bmi = calculate_bmi(meters, kg)
        print(f"Calculated BMI: {bmi}")
        classification = classify_bmi(bmi)
        print(f"Your BMI is classified as {classification}")
        write_csv(bmi)
        tracking_plot()
    except ValueError as e:
        sys.exit(e)

def check_height(height: str, unit_system: str) -> float:
    """
    Checks the unit system with a regex to see if it is in the expected format. If the unit system is metric, returns the float of the units.
    If it is imperial, converts the units and then returns the float of them.
    1 inch = 0.0254 meters
    1 foot = 12 inches
    """
        # METRIC SYSTEM VALIDATION
    if unit_system == "metric":
        # Validate that height is a numeric value
        if not re.match(r"^\d+(\.\d+)?$", height):
            raise ValueError("For metric system, please provide height as a numeric value without units (e.g., 1.75).")
        return float(height)

        # IMPERIAL SYSTEM VALIDATION
    if unit_system == "imperial":
        match = re.match(r"(\d+)\s*feet(?:\s*(\d*)\s*inch(?:es)?)?", height)
        if not match:
            raise ValueError("Invalid height. Please use the format: 'X feet Y inches'")
        feet = float(match.group(1))
        inches = float(match.group(2)) if match.group(2) else 0
        return round(((feet * 12) + inches) * 0.0254, 2)

def check_mass(mass: str, unit_system: str) -> float:
    """
    Checks the unit system and the input format with a regex, if the system is metric returns the mass in kg.
    If it is imperial, converts the mass to kg and then returns it.
    """
        # METRIC SYSTEM VALIDATION
    if unit_system == "metric":
        if not re.match(r"^([0-9]+.?[0-9]*)$", mass):
            raise ValueError("For metric system, please provide mass as a numeric value without units (e.g., 75).")
        return float(mass)

        # IMPERIAL SYSTEM VALIDATION
            # convert the mass from pounds to kg
    if unit_system == "imperial":
        if not re.match(r"^([0-9]+.?[0-9]*)$", mass):
            raise ValueError("For imperial system, please provide mass as a numeric value without units (e.g., 201).")
        return round(float(mass) / 2.205, 1)

def calculate_bmi(height_in_meters: float, mass_in_kg: float) -> float:
    """
    Calculates the BMI with given height and mass and returns the BMI.
    Depending on the unit system they might need to go through conversion into meters and kilograms using the functions check height and check mass.
    BMI = kg/m**2
    """
    return round(mass_in_kg / height_in_meters**2, 1)


def classify_bmi(bmi: float) -> str:
    """
    Classifies the BMI into different categories, returns a string with the class the BMI belongs to.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi <= 34.9:
        return "Obese Class I"
    elif 35 <= bmi <= 39.9:
        return "Obese Class II"
    elif bmi >= 40:
        return "Obese Class III"

def write_csv(bmi):
    """
    write a csv with two columns: 1. todays date. 2. BMI on that specific day.
    chekcs if the csv already exists, otherwise creates it and include the headers only on the first execution.
    """
    # Get the current datetime
    now = date.today()

    # Check if the csv file exists
    file_path = "bmi_overtime.csv"
    file_exists = os.path.isfile(file_path)

    #open csvfile (or creates it)
    with open("bmi_overtime.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames = ["timestamp", "bmi"])
    # Check if the file is empty or it's the first time writing
        if file.tell() == 0 or not file_exists:
            writer.writeheader()  # Write the header only if necessary
        # Write the data inserted on the command line arguments
        writer.writerow({"timestamp": now, "bmi": bmi})

def tracking_plot():
        # Read the CSV file with pandas
    df = pd.read_csv('bmi_overtime.csv')

    plt.plot(df['timestamp'], df['bmi'], label='BMI Over Time', color='gray', linestyle='--', marker='.')

    # Adding labels, title, and legend
    plt.xlabel('Date')
    plt.xticks(rotation=270, fontsize=8)
    plt.ylabel('Body Mass Index')
    plt.title('BMI Over Time')
    plt.legend()
    # Adding gridlines
    plt.grid(True)
    plt.tight_layout()
    # Annotating BMI classifications
    for index, row in df.iterrows():
        classification = classify_bmi(row['bmi'])
        plt.annotate(classification, (row['timestamp'], row['bmi']), textcoords="offset points", xytext=(0,-8), va='center', ha='center', fontsize=7, fontweight='bold')
    # Save the plot to a file
    plt.savefig('bmi_over_time.png', format='png')
    # Clear the plot to avoid overlap if the script runs multiple times
    plt.clf()

if __name__ == "__main__":
    main()
