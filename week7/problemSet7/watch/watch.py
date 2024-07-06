import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^<.+?src="(?:https?://)?(?:www\.)?youtube\.com/(?:\w+)/(\w+)".+?>$', s, re.IGNORECASE):
        link = "https://youtu.be/" + matches.group(1)
        return link


if __name__ == "__main__":
    main()
