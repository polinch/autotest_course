import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

numbers = [895, 896, 897, 898, 899, 903, 904, 905]


def calc():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', numbers)
def test_lesson_page(browser, number):
    link = f'https://stepik.org/lesson/236{number}/step/1'
    browser.get(link)
    browser.implicitly_wait(30)

    textarea = browser.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(calc())

    submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    submit_button.click()

    hint_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text

    assert hint_text == "Correct!", \
        f'Expected \'Correct!\' instead of \'{hint_text}\''
