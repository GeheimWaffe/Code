from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = Firefox()

# Define the target URL
url = 'https://app.powerbi.com/?route=home&noSignUpCheck=0'

# Maximize
driver.maximize_window()

# Navigate to the URL
driver.get(url)

# Authenticate
action = webdriver.ActionChains(driver)
action.send_keys('4090DQ')

#we = driver.find_element_by_tag_name('html')
#we.send_keys("4090DQ")

# print(we)
# driver.elem
# webdriver.ActionChaines(driver).send_keys("4").perform()
