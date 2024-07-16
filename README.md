# BMI Calculator and Tracker
#### Video Demo:  <https://www.youtube.com/watch?v=98S7JpGz1SY>

#### Description:
This Python project calculates Body Mass Index (BMI) based on user-provided height and weight, supports both metric and imperial units, and tracks BMI over time in a CSV file. It also includes classification of BMI into categories such as underweight, normal weight, overweight, and three classes of obesity.

## Features

### BMI Calculation and Classification

The core functionality of the project revolves around accurately computing BMI based on user-provided height and weight data. It employs standard formulas to ensure precise results and then classifies the BMI into various categories:

- **Underweight**: BMI below 18.5
- **Normal Weight**: BMI between 18.5 and 24.9
- **Overweight**: BMI between 25 and 29.9
- **Obese Class I**: BMI between 30 and 34.9
- **Obese Class II**: BMI between 35 and 39.9
- **Obese Class III**: BMI 40 and above

### Data Tracking and Visualization

#### CSV Data Storage

The project utilizes a CSV file (`bmi_overtime.csv`) to store BMI measurements along with timestamps. This allows users to track their BMI progression over days, weeks, months, or years.

#### Interactive Plotting

It includes a feature to generate interactive time series plots (`bmi_overtime.png`) using matplotlib. These graphs visually represent changes in BMI over the recorded period, aiding in trend analysis and long-term health management.

### Input Validation and Error Handling

#### Robust Input Handling

The program ensures robust input validation to prevent errors and provide a smooth user experience. It checks for correct formats in both metric and imperial units, guiding users to enter data accurately.

#### Error Messaging

In case of invalid inputs or unexpected errors, the program provides clear error messages. This helps users understand what went wrong and how to correct it, enhancing usability.

## Installation and Requirements

### Installation Steps

Ensure Python 3 is installed on your system. Then, install the necessary libraries using:

```bash
pip install -r requirements.txt
```

### Libraries that were used for this project

- `argparse`: For parsing command-line arguments.
- `re`: Regular expressions for input validation.
- `sys`: System-specific parameters and functions.
- `csv`: Reading and writing CSV files.
- `os`: Operating system interface for file operations.
- `datetime`: Handling dates and times.
- `pandas`: Data manipulation.
- `matplotlib`: Plotting graphs for the time series visualization.

## Usage

### Getting Started

To calculate your BMI and begin tracking, execute `project.py` with the following command format:

```bash
python project.py --height <height_value> --mass <mass_value> -s <unit_system>
```

Replace `<height_value>` with your height (in meters or feet/inches) and `<mass_value>` with your weight (in kilograms or pounds). Specify `-s metric` or `-s imperial` for the respective unit system.

#### Example Usage

```bash
python project.py --height 1.75 --mass 70 -s metric
```

### Output and Results

Upon execution, the program computes your BMI, classifies it into a category, and displays the result. It appends this data along with a timestamp to `bmi_overtime.csv`. Additionally, it generates `bmi_overtime.png`, a visual representation of your BMI changes over time.

## Example of visualization and tracking
![preview](https://github.com/user-attachments/assets/aefa93fd-7f85-4a92-9366-817e1021d202)

## Example CSV

Here is an example of the `bmi_overtime.csv` file that the program generates and appends to:

```csv
timestamp,bmi
2023-08-01,23.7
2023-25-02,24.2
2023-07-03,24.0
2023-17-04,24.8
2023-12-05,25.0
2023-02-06,25.7
2023-01-07,25.9
2023-15-08,26.9
2023-19-09,25.2
2023-23-10,24.5
2023-08-11,23.7
2023-25-12,24.2
2024-07-01,24.0
2024-17-02,24.8
2024-12-03,25.0
2024-02-04,25.7
2024-01-05,25.9
2024-15-06,26.9
2024-19-07,25.2
2024-23-08,25.5
```
