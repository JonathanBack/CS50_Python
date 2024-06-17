'''
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably
bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800,
3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on
September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD)
order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes
as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636
or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
'''
months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
]

while True:
    date = input("Date: ").strip()

    #mm/dd/yyyy // 08/09/2003
    if "/" in date:
        month, day, year = date.split("/")

    #Month day, yyyy // April 2, 2005
    elif "," in date:
        month, day, year = date.split()
        if month in months:
            month = months.index(month)
            month += 1
            day = day.strip(",")

    else:
        continue
    try:
        if int(day) > 31 or int(month) > 12:
            continue
        else:
            break
    except ValueError:
        continue

day = int(day)
month = int(month)

print(f"{year}-{month:02}-{day:02}")



