import requests

res = requests.get('http://127.0.0.1:5001/users/get_user_data/2')
if res.ok:
    print(res.status_code)

response = requests.put('http://127.0.0.1:5000/users/2', json={"name": "George"})
user_id= 2
if response.status_code == 200:
    print(response.text)