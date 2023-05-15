import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    #driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://google.com")
    assert driver.title == "Google"
    driver.close()
