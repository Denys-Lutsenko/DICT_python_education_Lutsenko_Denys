import requests

file = open("source.html", "wb")
url = input("Input the URL: ")
response = requests.get(url)
status_code = response.status_code
if status_code == 200:
    file.write(response.content)
    print("Content saved.")
else:
    print(f"The URL returned {status_code}!")

file.close()