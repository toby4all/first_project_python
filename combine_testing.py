import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# request to post new data to database with usr_name 'John'
res = requests.post('http://127.0.0.1:5000/users/6', json={"name": "Victoria"})
if res.status_code == 200:
    print(res.json())

# request to get data from database with usr_id '6'
response = requests.get('http://127.0.0.1:5000/users/6')
if response.status_code == 200:
    print(response.text)

# query database to make sure username is stored under id:'6'

schema_name = "mydb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id ='6' ")

# Iterating table to print the user details on the row with this user_id.
for row in cursor:
    print(row)

cursor.close()
conn.close()

driver = webdriver.Chrome(service=Service("C:/Users/Toby/Desktop/Global dev ops/chromedriver-win64/chromedriver-win64/chromedriver.exe"))
driver.implicitly_wait(10)
driver.get('http://127.0.0.1:5001/users/get_user_data/1')
print(driver.current_url)
try:
    elements = driver.find_element(By.ID, 'user')
    print(elements.text)
except Service:
    print('No such user')
finally:
    print(elements.text)

