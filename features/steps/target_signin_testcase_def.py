from selenium.webdriver.common.by import By
from behave import  given, when,  then
from time import sleep


@when('Click Sign In')
def click_signin(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(6)



@when('From right side navigation menu, click Sign In')
def click_signin_right(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(5)



@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert 'Sign into your Target account' in actual_text, f'Error! Text Sign into your Target account not in {actual_text}'




