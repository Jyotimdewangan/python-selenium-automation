from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# click on signin button
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

# Click Signin from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(6)

# Verification
actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert 'Sign into your Target account' in actual_text, f'Error! Text Sign into your Target account not in {actual_text}'

print("test passed")
driver.quit()