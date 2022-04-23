import requests

url = input("Input the URL: ")
response = requests.get(url)
print(response.json().get("content")) if "content" in response.json() and response.status_code == 200 \
    else print("Invalid quote resource!")