from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import winsound


def openfirefox():
    driver = webdriver.Firefox(executable_path="C:\\Users\\hp\\Downloads\\geckodriver-v0.27.0-win64\\geckodriver.exe")
    driver.get("https://stackoverflow.com/")
    # driver.implicitly_wait(3600)
    driver.find_element_by_xpath("//li[@class='-ctas']/a").click()
    driver.find_element_by_xpath("//div[@id='openid-buttons']/button[1]").click()
    # put your google account here
    driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("google_account")
    driver.find_element_by_xpath("//span[text()='Next']//following-sibling::div").click()
    time.sleep(2)
    # put your google account password here
    driver.find_element_by_xpath("//input[@type='password']//parent::div/input").send_keys("password")
    driver.find_element_by_xpath("//span[contains(text(),'Next')]/following-sibling::div").click()
    driver.get("https://meet.google.com/ixx-viep-mou")
    time.sleep(3)
    driver.find_element_by_xpath("//div[@aria-label='Turn off microphone (CTRL + D)']").click()
    driver.find_element_by_xpath("//div[@aria-label='Turn off camera (CTRL + E)']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//span[text()='Join now']//parent::span//parent::div").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[@data-tooltip='Chat with everyone']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//textarea[@aria-label='Send a message to everyone']").send_keys("Hello guys")
    driver.find_element_by_xpath("//div[@data-tooltip='Send message']").click()
    result = WebDriverWait(driver, 3600).until(ec.text_to_be_present_in_element((By.XPATH, "//div[@data-message-text='hello']"), 'hello'))
    if result is not None:
        print("we are going to put the id")
    time.sleep(1)
    driver.find_element_by_xpath("//textarea[@aria-label='Send a message to everyone']").send_keys("19115")
    driver.find_element_by_xpath("//div[@data-tooltip='Send message']").click()
    winsound.Beep(2500, 1000)


def openchrome():
    driverlocation = "C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverlocation
    driver = webdriver.Chrome(driverlocation)
    driver.get("https://letskodeit.teachable.com/p/practice")
    result = driver.find_element_by_id("name")
    print(result)


# openchrome()
openfirefox()
