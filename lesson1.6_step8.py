import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(by=By.TAG_NAME, value="input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


