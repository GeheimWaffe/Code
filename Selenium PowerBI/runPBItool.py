#*** Script written to export automatically data from powerbi
#*** Author: Vincent Scherrer

import time
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = Firefox(executable_path='/opt/WebDriver/bin/geckodriver')


# Maximize
driver.maximize_window()

# Define the target URL and navigate to it
url = 'https://app.powerbi.com/?route=home&noSignUpCheck=0'
driver.get(url)

# Enter user name
driver.find_element_by_id('i0116').send_keys('4090DQ@tera.infragaz.com')

# Validate
driver.find_element_by_id('idSIButton9').click()

# wait for the next screen
time.sleep(2)

# Enter password
driver.find_element_by_id('i0118').send_keys('2031Vinc3nt')
# Validate
driver.find_element_by_id('idSIButton9').click()

# wait for the next screen
time.sleep(1)

# confirm stay connected
driver.find_element_by_id('KmsiCheckboxField').click()
driver.find_element_by_id('idSIButton9').click()

# wait for loading
time.sleep(2)

# We're now on the PowerBI Main page.Let's go to the reporting DF
driver.get('https://app.powerbi.com/groups/me/reports/f782fcc6-d2f0-4828-a81b-98d41d7852dd/ReportSection8ecdafa8076f8e9c357e')

# Wait sufficiently so that the report can load asynchronously
time.sleep(10)

# get the tabl
detailedTable = driver.find_element_by_class_name('visual.visual-tableEx.allow-deferred-rendering')
print('*** Detailed table found')

# Open the menu
detailedTable.click()
time.sleep(1)

menuBtn = driver.find_element_by_class_name('vcMenuBtn')
print('*** Table menu button found')
menuBtn.click()

for el in driver.find_elements_by_class_name('label.hasIcon'):
    print('*** Export Option found')
    if el.get_attribute('aria-posinset') == '3':
        print('*** Preparing data export !')
        el.click()

        # Export
        driver.find_element_by_class_name('primary').click()
