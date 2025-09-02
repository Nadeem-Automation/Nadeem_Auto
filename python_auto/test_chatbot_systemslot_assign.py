import time
import random
from playwright.sync_api import Page, expect

def test_chatbot_system_slot_assign(page:Page):
    page.goto("https://mqa2.xavlab.xyz/")
    page.get_by_label("Email").fill("testing1mna@gmail.com")
    page.get_by_role("button").click()
    page.get_by_placeholder("Enter domain").fill("xd")
    page.get_by_role("button").click()
    page.get_by_placeholder("Enter password").fill("Password@1")
    page.get_by_role("button").click()
    
    time.sleep(2)


