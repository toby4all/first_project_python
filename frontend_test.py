from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:/Users/Toby/Desktop/Global dev ops/chromedriver-win64/chromedriver-win64/chromedriver.exe"))
driver.implicitly_wait(10)
driver.get('http://127.0.0.1:5001/users/get_user_data/2')
print(driver.current_url)

elements = driver.find_element(By.ID, value='user')
elements.get_attribute('user')
print(elements.text)

elements = driver.find_element(By.ID, value='no-user')
elements.get_attribute('no-user')
print(elements.text)