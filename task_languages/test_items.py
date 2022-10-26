import time


from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_cart_exist(browser):
    browser.get(link)
    # Для проверки установки выбранного при запуске теста языка
    time.sleep(30)
    button_add_to_cart = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button_add_to_cart is not None, \
        "Button \'Add to cart\' does not exist"
