import requests
import json

r = requests.get(f"http://www.floatrates.com/daily/{input()}.json")

dictionary = json.loads(r.text)
print(dictionary['usd'])
print(dictionary['eur'])