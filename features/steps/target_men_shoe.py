from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
COLOR_OPTIONS = (By.CSS_SELECTOR, '[aria-label="Carousel"] ul li')
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")
#sel_color = (By.XPATH, "//picture[@class='styles__StyledFadeInPicture-sc-12vb1rw-0 jihssy']")


@given('Open target Sneaker Shoe page')
def th_colors(context):
    context.driver.get("https://www.target.com/p/A-54631909")


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_color = ['Black', 'Gray', 'White','Red', 'Green', 'Yellow']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_color == actual_colors, f'Expected {expected_color} did not match actual {actual_colors}'