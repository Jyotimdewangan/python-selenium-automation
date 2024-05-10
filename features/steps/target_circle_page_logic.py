from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


BENEFIT_CELLS=(By.XPATH, "//div[@class='styles__CellBlocksContainer-sc-3f68hg-1 fbpFkx']")


@given('Open target circle page')
def open_circle_pg(context):
    context.driver.get("https://www.target.com/circle")


@then('Varify {expected_num} benefits cells on circle page')
def varify_3_benefits(context, expected_num):
    expected_num = int(expected_num)
    actual_num = context.driver.find_elements(*BENEFIT_CELLS)
    assert expected_num == len(actual_num), f'Error! Expected {expected_num} but got {len(actual_num)}'


