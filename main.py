import requests

response = requests.get("https://api.scratch.mit.edu/projects/1000000")
print(response.json())