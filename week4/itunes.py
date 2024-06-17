#APIs (Aplication program interface) & JSON (Javascript object notation) -> python can read or write json as well
#using itunes API
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response= requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

#o = json.dumps(response.json(),indent = 2)
o = response.json()
#print(o["results"])

#print(len(o["results"]))

for result in o["results"]:
    print(result["trackName"])
