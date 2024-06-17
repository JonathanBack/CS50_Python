import sys
import requests
#import json

try:
    n = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")

except IndexError:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

except requests.RequestException:
    sys.exit()

#o = json.dumps(response.json(),indent = 2)
bitcoin_info = response.json()
amount = float((bitcoin_info["bpi"]["USD"]["rate_float"]))

amount = amount * n

print(f"${amount:,.4f}")

