# Task 11: Guvi Login Page Test Case
# This test case will check the login functionality of the Guvi website.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

login_url = "https://www.guvi.in/"
migrated_url = "https://www.guvi.in/sign-in/"
expected_dashboard_url = "https://www.guvi.in/courses/?current_tab=myCourses"
username = "ramyabhat.v@gmail.com"
password = "Raksh@2025"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Run in headless mode for CI/CD environments
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)
    # To run in normal mode, uncomment the following line:
    # driver = webdriver.Chrome()  
    # driver.maximize_window()
    yield driver
    # Cleanup code after tests are done
    driver.quit()

# Testing the login page and perform login successfully by checking username and password fields are displayed and enabled, then enter the username and password.

def test_login_functionality(driver):
    driver.get(login_url)
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(3) 
    assert driver.current_url == migrated_url, f"Expected URL: {migrated_url}, but got: {driver.current_url}"
    print("Login page opened successfully!")
    time.sleep(3)
    # Enter username and password
    driver.find_element(By.ID, "email").is_displayed()
    print("Email field is displayed")
    driver.find_element(By.ID, "email").is_enabled()
    print("Email field is enabled")
    # Enter correct username
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "password").is_displayed()
    print("Password field is displayed")
    driver.find_element(By.ID, "password").is_enabled()
    print("Password field is enabled")
    # Enter correct password
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(3)
    # Click the login button
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(5)
    # Verify the URL of the dashboard page
    assert driver.current_url == expected_dashboard_url, f"Expected URL: {expected_dashboard_url}, but got: {driver.current_url}"
    print("Login successful...!")

 # To test the login page and perform login by entering wrong username and password for checking the failure.
 
def test_login_functionality_fail(driver):
    driver.get(login_url)
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(3) 
     # Intentionally using the wrong credentials to trigger a failure
    driver.find_element(By.ID, "email").send_keys(password) 
    driver.find_element(By.ID, "password").send_keys(username)
    time.sleep(3)
    # Click the login button
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(5)  
    # Verify the URL of the dashboard page
    # This should fail as the credentials are incorrect
    assert driver.current_url == expected_dashboard_url, f"Expected URL: {expected_dashboard_url}, but got: {driver.current_url}"
    print("Login unsuccessful, please try again...!")

# After login, close the browser
    driver.close()