'''
A short and simple test case file.
Intention to learn and attempt test abilities using unittest.
'''

# Importing the selenium libraries
import selenium.common.exceptions as exceptions
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Pre-defined variables
fyc_url = "https://indeedemo-fyc.watch.indee.tv/"
PIN = "WVMVHWBS"

class AutomateVideo(unittest.TestCase):

    # Use class method to reduce resource for testing
    @classmethod
    def setUp(inst):
        # Initialise the driver for Firefox
        inst.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        inst.driver.maximise_window()

        # Open the fyc link to the website
        try:
            inst.driver.get(fyc_url)
        except exceptions.InsecureCertificateException as e:
            print("Hit insecure certificate.")

    def test_login(self):
        # Using XPATH to find the pin and sign-in element in the login page
        try:
            pin_element = self.driver.find_element(By.XPATH, "//input[@id='pin']")
            sign_in_element = self.driver.find_element(By.XPATH, "//button[@id='sign-in-button']")
        except exceptions as e:
            raise Exception(e)
        else:
            pin_element.send_keys(PIN)
            sign_in_element.submit()
        # assert

    @classmethod
    def tearDown(inst):
        # Close the session
        inst.driver.quit()

if __name__ == "__main__":
    unittest.main()