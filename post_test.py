import requests

url = 'http://127.0.0.1:5000/users/4'
user_id = 4
res = requests.post(url, json={"name": "Maxwell"})
print(res.status_code)
# if res.status_code ==200:
#     print('User added successfully')
# else:
#     print('Error adding user:', res.text)
