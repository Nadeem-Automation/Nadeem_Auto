import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_login():
    option1 = Options()
    option1.add_argument('--no-sandbox')
    option1.add_argument('--window-size=1420,1080')
    option1.add_argument('--headless')
    option1.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=option1)
    driver.implicitly_wait(10)
    driver.get("https://google.com")
    assert driver.title == "Google"
    assert driver.title == "asdfasdf"
    driver.close()
