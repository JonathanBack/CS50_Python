    # infer from the URL the username of their account

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")

import re


    # re.sub(pattern, repl, string, count=0, flags=0). repl = replacement string, count = how many times
    # USEFUL for cleaning data
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

    # re.search
    # (?:...) tells re.search() to NOT store that group in the return values

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1)) # the only group being returned is (.+), which is username
