import time
import random
from playwright.sync_api import Page, expect

def test_chatbot_system_slot_assign(page:Page):
    page.goto("https://mqa2.xavlab.xyz/")
    page.get_by_label("Email").fill("malik.anwar@telusinternational.com")
    page.get_by_role("button").click()
    page.get_by_placeholder("Enter domain").fill("xd")
    page.get_by_role("button").click()
    page.get_by_placeholder("Enter password").fill("Password@2")
    page.get_by_role("button").click()
    BOT_NAME = 'Transaction Bot MQA'
    Folder_Name = "QA_Nadeem"
    Sub_Folder_Name = "Nadeem_Automation_Dont_Delete"
    Interaction_Name = "Settings_Tags"
    Intent_Name = "Tags"
    page.locator("//a[@href='/chat-bot']").click()
    page.locator(f"//h6[normalize-space()='{BOT_NAME}']").click()
    page.locator(f"//span[@title='{Folder_Name}']").click()
    page.locator(f"//span[@title='{Sub_Folder_Name}']").click()
    page.locator(f"//span[@title='{Interaction_Name}']").click()
    page.locator(f"//div[@title='{Intent_Name}']").click()
    page.locator("//div[@class='button-wrapper']//span[contains(text(),'Edit')]").click()
    time.sleep(2)
    text = page.locator("//div[@class='ql-editor']")
    text.scroll_into_view_if_needed(timeout=3000)  # Scroll through the dropdown until the desired element is reached.
    text.wait_for(state="visible", timeout=5000)
    text.click()
    page.keyboard.type("{{")
    time.sleep(2)
    page.locator("//input[@placeholder='Select Scope']").click()
    scope = page.locator("//a[@data-testid='if-dropdown-item-marT']")
    for j in range(scope.count()):
        scope1 = scope.nth(j)
        if scope1.text_content() == "sys":
            scope1.scroll_into_view_if_needed(timeout=3000)
            scope1.wait_for(state="visible", timeout=5000)
            scope1.click()
            break
    time.sleep(2)

    page.locator("//div[@class='select__input-container css-1duuv5x']").click()
    slot = page.locator("//div[@class='slotoptions title-ellipsis']")
    for j in range(slot.count()):
        slot1 = slot.nth(j)
        if slot1.text_content() == "UserQuery":
            slot1.scroll_into_view_if_needed(timeout=3000)
            slot1.wait_for(state="visible", timeout=5000)
            slot1.click()
            break
    time.sleep(2)
    page.locator("//input[@value='Done']").click()
    time.sleep(5)


