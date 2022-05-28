import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    labels = browser.find_elements(by=By.TAG_NAME, value="label")
    inputs = browser.find_elements(by=By.TAG_NAME, value="input")

    for i, label in enumerate(labels):
        if label.text[-1] == "*":
            inputs[i].send_keys("TEXT")

    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(by=By.TAG_NAME, value="h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()