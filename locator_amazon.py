from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')
sleep(10)
driver.find_element(By.XPATH, "//*[@id='nav-link-accountList-nav-line-1']").click()
# By XPATH
driver.find_element(By.XPATH, "//*[@aria-label='Amazon']")
driver.find_element(By.XPATH, "//*[@class='a-icon a-icon-logo']")
#driver.find_element(By.XPATH, "//*[text()='metadata1']")
#driver.find_element(By.XPATH, "//input[@class='a-spacing-small']")
sleep(10)
driver.find_element(By.ID, 'authportal-main-section')
driver.find_element(By.XPATH, "//*[@class='a-section']")
sleep(10)

#Amazon logo
driver.find_element(By.XPATH, "//*[@class='a-icon a-icon-logo']")
#driver.find_element(By.XPATH, "//*[@role='img']")
#driver.find_element(By.XPATH, "//*[@aria-label='Amazon']")


#Signin field
driver.find_element(By.XPATH, "//*[@class='a-spacing-small']")


# Continue button
driver.find_element(By.ID, 'continue')
#driver.find_element(By.XPATH, "//input[@type='submit']")
#driver.find_element(By.XPATH, "//*[@class='a-form-label']")


#Conditions of use link
driver.find_element(By.ID, "legalTextRow")

#Privacy notice link
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")

#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#driver.find_element(By.XPATH, "//*[text()='Need help?']")



#create Amazon account link
driver.find_element(By.ID, "createAccountSubmit")

#Shop on Amazon Business link
#driver.find_element(By.XPATH, "//*[text()='Shop on Amazon Business']")
driver.find_element(By.ID, "ab-sign-in-ingress-link")

#Forgot your password link(I did nit find this on my amazon page)

#Other issues with Sign-In link (I did nit find this on my amazon page)

print('Test Passed!')
driver.quit()








