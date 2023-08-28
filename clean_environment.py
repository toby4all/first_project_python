import requests

res = requests.get('http://127.0.0.1:5000/stop_server')
if res.ok:
    print(res.text)

response = requests.get('http://127.0.0.1:5001/stop_server')
if response.status_code == 200:
    print(response.text)