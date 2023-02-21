from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("/Users/dapoaowolabi/Downloads/chromedriver")
def get_driver():
# Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def main():
    driver = get_driver()
    driver.find_element(By.ID,"id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID,"id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/nav/div/a').click()
    time.sleep(2)
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/h1[2]')
    element = element.text
    element = element.split(": ")
    element = float(element[1])
    print(driver.current_url, element)
    

#print("success")
print(main())