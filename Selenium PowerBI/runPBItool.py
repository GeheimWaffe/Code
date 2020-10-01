#*** Script written to export automatically data from powerbi
#*** Author: Vincent Scherrer

import time
import io
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def exportReportingGestion(targetFolder, username, userpassword, executablepath):
    """ Function which enables the download of the detailed reporting gestion table
    :target Folder : the folder to which the extract should be downloaded"""
    # Create a profile for automatic download
    # Note : to find the current user profile, type in
    fxProfile = FirefoxProfile()

    fxProfile.set_preference('browser.download.folderList',2)
    fxProfile.set_preference('browser.download.manager.showWhenStarting', False)
    fxProfile.set_preference('browser.download.dir',targetFolder)
    # Works ! Note that the MIME type has to be exactly right and correspond to xlsx
    fxProfile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    driver = Firefox(firefox_profile=fxProfile, executable_path='/opt/WebDriver/bin/geckodriver')

    # Maximize
    driver.maximize_window()

    # Define the target URL and navigate to it
    url = 'https://app.powerbi.com/?route=home&noSignUpCheck=0'
    driver.get(url)

    # Enter user name
    driver.find_element_by_id('i0116').send_keys(username)

    # Validate
    driver.find_element_by_id('idSIButton9').click()

    # wait for the next screen
    time.sleep(2)

    # Enter password
    driver.find_element_by_id('i0118').send_keys(userpassword)
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

            # Validate the export
            time.sleep(1)
            driver.find_element_by_class_name('primary').click()

# Main method
# *** geckodriver path for Ubuntu
# exPath = '/opt/WebDriver/bin/geckodriver'
# *** geckodriver path for Windows

# Target Path
# Ubuntu
tgPath = '~/Documents/'
# Windows
tgpath = 'C:\\Users\\4090DQ\\GRTgaz\\Pilotage Budget & Ressources DSI - General'

exPath = 'C:/Users/4090DQ/OneDrive - GRTgaz/Développement/python/geckodriver/geckodriver.exe'
un = str(raw_input('Identifiant FARO ? \n'))
un += '@tera.infragaz.com'
up = str(raw_input('User password ? \n'))
exportReportingGestion(tgPath, un, up, exPath)
