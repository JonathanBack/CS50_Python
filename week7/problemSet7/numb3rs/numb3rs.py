import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        parts = ip.split(".")

        for part in parts:
            if int(part) > 255 or int(part) < 0:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()

