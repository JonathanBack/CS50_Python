import re


def main():
    print(convert(input("Hours: ")))

def convert(s):
    dict = {
    "12 AM": "00",
    "1 AM": "01",
    "2 AM": "02",
    "3 AM": "03",
    "4 AM": "04",
    "5 AM": "05",
    "6 AM": "06",
    "7 AM": "07",
    "8 AM": "08",
    "9 AM": "09",
    "10 AM": "10",
    "11 AM": "11",
    "12 PM": "12",
    "1 PM": "13",
    "2 PM": "14",
    "3 PM": "15",
    "4 PM": "16",
    "5 PM": "17",
    "6 PM": "18",
    "7 PM": "19",
    "8 PM": "20",
    "9 PM": "21",
    "10 PM": "22",
    "11 PM": "23"
}

    if matches := re.search(r"^(\d+):?(\d+)? (AM |PM )(?:to)? (\d+):?(\d+)? (AM|PM)", s):
        start_hour, start_minute, start_period, end_hour, end_minute, end_period = matches.groups()

        if start_minute == None:
            start_minute = "00"

        if end_minute == None:
            end_minute = "00"

        if int(start_minute) > 59 or int(end_minute) > 59 or int(start_hour) > 12 or int(end_hour) > 12 :
            raise ValueError

        new_start = dict[start_hour + " " + start_period.strip()] + ":" + start_minute
        new_end = dict[end_hour + " " + end_period.strip()] +  ":" + end_minute
        new_hour = new_start  + " to " + new_end

        return new_hour


    else:
        raise ValueError

if __name__ == "__main__":
    main()
