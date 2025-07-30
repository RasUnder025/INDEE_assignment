'''
Author: Clifford
INDEE Assignment: Automate video playback
'''

# Importing the selenium libraries
import selenium.common.exceptions as exceptions
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Pre-defined variables
fyc_url = "https://indeedemo-fyc.watch.indee.tv/"
PIN = "WVMVHWBS"

# Initialise the driver for Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# Initialise the WebDriverWait for 10 seconds
wait = WebDriverWait(driver, 10)

# Open the fyc link to the website
try:
    driver.get(fyc_url)
except exceptions.InsecureCertificateException as e:
    print("Hit insecure certificate.")

# Using XPATH to find the pin and sign-in element in the login page
try:
    pin_element = wait.until(
        EC.visibility_of_element_located((
            By.XPATH, "//input[@id='pin']"
            )))
except exceptions.NoSuchElementException as e:
    raise Exception(e)
else:
    pin_element.send_keys(PIN)
    pin_element.submit()

# Using XPATH to navigate through the Tiles
try:
    title_element = wait.until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[@id='brd-01fvc8gs4sa9kjs8wxs6gnsn76']"
            )))
except exceptions as e:
    raise Exception(e)
else:
    title_element.click()

action = ActionChains(driver)

# Using action chain to find the Test automation project and interact with it
try:
    project_element = wait.until(
        EC.element_to_be_clickable((
            By.XPATH, "//h5[text()='Test automation project']"
            )))
except exceptions as e:
    raise Exception(e)

# Firefox doesn't support scroll, so add the script
try:
    action.move_to_element(project_element).click().perform()
except exceptions.MoveTargetOutOfBoundsException as e:
    print("Scrolling to the element")
    driver.execute_script("arguments[0].scrollIntoView(true);", project_element)
    action.move_to_element(project_element).click().perform()

# Using XPATH to locate the play button and click
try:
    play_element = wait.until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[@aria-label='Play Video']"
            )))
except exceptions as e:
    raise Exception(e)

# Firefox doesn't support scroll, so add the script
try:
    action.move_to_element(play_element).click().perform()
except exceptions.MoveTargetOutOfBoundsException as e:
    print("Scrolling to the element")
    driver.execute_script("arguments[0].scrollIntoView(true);", play_element)
    action.move_to_element(play_element).click().perform()

# Video is not supported on my browser

# Playing for 10 seconds
time.sleep(10)

# Reverting back through action keys navigation
driver.execute_script("window.history.go(-2)")

# Using CSS to find the sidebar, then click the logout icon using JavaScript
try:
    wait.until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, "#SideBar"
        )))
    logout_element = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[id='signOutSideBar']" 
            )))
    driver.execute_script("arguments[0].click();", logout_element)
except exceptions.NoSuchElementException as e:
    raise Exception(e)

# Close the session
wait.until(
    EC.visibility_of_element_located((
        By.XPATH, "//img[@id='form-logo-image']"
    )))
driver.quit()