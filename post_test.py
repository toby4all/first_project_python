import requests

res = requests.post('http://127.0.0.1:5000/users/3', json={"name": "Oluwatobi"})

print(res.status_code)
# print(res.json())
