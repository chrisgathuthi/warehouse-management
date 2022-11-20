import requests
from getpass import getpass

auth_point = "http://127.0.0.1:8000/api/auth/"
password = getpass("key-in password\n: ")

auth_response = requests.post(auth_point,json={"username":"chris","password":password})
print(auth_response.json())