import requests as re

base="http://127.0.0.1:5000/"

response=re.get(base+"/h/"+"sid")
print(response.json())