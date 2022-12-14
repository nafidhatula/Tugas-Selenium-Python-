import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)
    
    def test_b_failed_login_with_username_and_password_incorrect(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        #validasi
        response_message = browser.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_c_failed_login_with_username_incorrect(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        #validasi
        response_message = browser.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_d_failed_login_with_password_incorrect(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        #validasi
        response_message = browser.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_e_failed_login_with_empty_username_and_password(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        #validasi
        response_message = browser.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3").text
        self.assertEqual(response_message, 'Epic sadface: Username is required')

        

    def tearDown(self):     
        self.browser.close()

if __name__ == '__main__':
    unittest.main()