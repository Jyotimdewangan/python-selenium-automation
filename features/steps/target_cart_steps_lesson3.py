from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
sleep(5)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
sleep(5)


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    #context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")

