import requests

res = requests.get('http://127.0.0.1:5000/users/get_user_data/2')
if res.ok:
    print(res.status_code)