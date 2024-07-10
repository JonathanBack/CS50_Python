import re
from datetime import date, datetime
import sys
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os

# Get the current datetime
now = datetime.now()

# Remove microseconds by setting them to zero
now = now.replace(microsecond=0)

# Check if the file exists
file_path = "bmi_overtime.csv"
file_exists = os.path.isfile(file_path)

with open("bmi_overtime.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["timestamp", "bmi"])

 # Check if the file is empty or it's the first time writing
    if file.tell() == 0 or not file_exists:
        writer.writeheader()  # Write the header

    # Write the data
    writer.writerow({"timestamp": now, "bmi": bmi})
