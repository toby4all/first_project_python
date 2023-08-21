import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# request to post new data to database with usr_name 'John'
res = requests.post('http://127.0.0.1:5000/users/3', json={"name": "Oluwatobi"})
if res.ok:
    print(res.status_code)
    print(res.json())

# request to get data from database with usr_id '2'
response = requests.get('http://127.0.0.1:5000/users/get_user_data/2')
if response.ok:
    print(response.status_code)

# query database to make sure username is stored under id:'1'

schema_name = "mydb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id ='2' ")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()

driver = webdriver.Chrome(service=Service("C:/Users/Toby/Desktop/Global dev ops/chromedriver.exe"))
driver.implicitly_wait(10)
driver.get('http://127.0.0.1:5000/users/2')
print(driver.current_url)

elements = driver.find_element(By.ID, 'user')
print(elements.text)

elements = driver.find_element(By.ID, 'no-user')
print(elements.text)