import pandas as pd
import matplotlib.pyplot as plt
import csv

# Read the CSV file
df = pd.read_csv('bmi_overtime.csv')

# Convert the 'timestamp' column to datetime

df['timestamp'] = pd.to_datetime(df['timestamp'])

# Plot the data with customizations
plt.plot(df['timestamp'], df['bmi'], label='BMI Over Time', color='blue', linestyle='--', marker='o')

# Adding labels, title, and legend
plt.xlabel('Date')
plt.ylabel('BMI')
plt.title('BMI Over Time')
plt.legend()

# Adding gridlines
plt.grid(True)

# Save the plot to a file
plt.savefig('bmi_over_time.png', format='png')

# Clear the plot to avoid overlap if the script runs multiple times
plt.clf()
