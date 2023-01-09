from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
import time

TINDER_URL = "https://tinder.com/"

FACEBOOK_LOGIN = "some_email"
FACEBOOK_PASSWORD = "some password"

chrome_driver_path = "C:/Software/Development/chromedriver.exe"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get(TINDER_URL)


def sign_in_to_tinder():
    # Sign in to Tinder using Facebook Login, Allows location, dismisses notifications upon login
    time.sleep(3)
    login_button = driver.find_elements(By.CSS_SELECTOR, "div.l17p5q9z")[1]
    login_button.click()
    time.sleep(1)
    driver.maximize_window()
    tinder_window = driver.window_handles[0]
    print(driver.title)
    accept_cookies = driver.find_element(By.XPATH, "//*[@id='q243527110']/div/div[2]/div/div/div[1]/div[1]/button")
    accept_cookies.click()
    login_with_facebook = driver.find_element(By.XPATH, "//*[@id='q-1484853966']/main/div/div[1]/div/div/div[3]/span/div[2]/button")
    login_with_facebook.click()
    time.sleep(2)
    driver.maximize_window()
    fb_window = driver.window_handles[1]
    driver.switch_to.window(fb_window)
    print(driver.title)
    time.sleep(2)
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(FACEBOOK_LOGIN)
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(FACEBOOK_PASSWORD)
    password_input.send_keys(Keys.ENTER)
    time.sleep(7)
    driver.switch_to.window(tinder_window)
    print(driver.title)
    location_button = driver.find_element(By.XPATH, "//*[@id='q-1484853966']/main/div/div/div/div[3]/button[1]")
    location_button.click()
    notifications_button = driver.find_element(By.XPATH, "//*[@id='q-1484853966']/main/div/div/div/div[3]/button[2]")
    notifications_button.click()
    time.sleep(7)


def swipe_right():
    # Use the web-based "like" button to find a match. Presses dismiss button if you get matched while swiping
    like_button = driver.find_element(By.XPATH, "//*[@id='q243527110']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]")
    for i in range(100):
        try:
            like_button.click()
            time.sleep(1)

        except NoSuchElementException:
            print("Like button not available")
            time.sleep(2)
            continue
        except ElementClickInterceptedException:
            back_to_tinder = driver.find_element(By.XPATH, "//*[@id='q573898311']/main/div/div[1]/div/div[4]")
            back_to_tinder.click()
            time.sleep(2)
            continue


sign_in_to_tinder()
swipe_right()

driver.quit()
