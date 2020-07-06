from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# change this below
ac_id = "enter your amarillo college id here"
ac_pass = "enter your amarillo college password here"

# load default profile with previusly installed extension
print("Loading default profile...")
profile = webdriver.FirefoxProfile('/Users/konyein/Library/Application Support/Firefox/Profiles/x562km7p.default-release')
driver = webdriver.Firefox(profile)

# get url
print("Going to actx.edu...")
driver.get("https://actx.blackboard.com/webapps/login/")
driver.maximize_window()

# enter username
print("Entering username...")
username = driver.find_element(By.NAME, "user_id")
username.send_keys(ac_id)

# enter password
print("Entering password...")
password = driver.find_element(By.NAME, "password")
password.send_keys(ac_pass)

# cookies alert dialog box
# driver.find_element_by_xpath("//*[@id='agree_button']").click()

# wait 1 sec to make sure everything is loaded
print("Waiting 1 seconds...")
time.sleep(1)

# click login
print("Logging in now...")
driver.find_element_by_xpath("//*[@id='entry-login']").click()
