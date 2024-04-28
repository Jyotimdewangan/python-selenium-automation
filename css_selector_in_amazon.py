from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

#create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')
sleep(15)
#nav-link-accountList
driver.find_element(By.ID,"nav-link-accountList").click()
sleep(5)
# click on  create amazon account
driver.find_element(By.CSS_SELECTOR,"#createAccountSubmit").click()
#driver.find_element(By.XPATH, "//a[text()='Create your Amazon account']")
sleep(5)
#open create your amazon account
#driver.find_element(By.ID,"createAccountSubmit").click()

#find registration page by clicking on start here text
#driver.find_element(By.XPATH, "//a[text()='Start here']").click()

#find Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

#create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#your name field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
#driver.find_element(By.ID,'ap_customer_name')

#email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")
#driver.find_element(By.ID,'ap_email')

#find password field
driver.find_element(By.CSS_SELECTOR,"#ap_password")
#driver.find_element(By.ID,'ap_password')

# find re enter password field
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")
#driver.find_element(By.ID,'ap_password_check')

#find continue (find create your amazon account)
driver.find_element(By.CSS_SELECTOR,"#continue")
#driver.find_element(By.ID,'Continue')


#find Conditions of use:
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")



# find Privacy Notice:
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#find sign in button
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')

print("test passed")

quit()