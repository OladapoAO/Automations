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
    driver.get("https://www.nike.com/ca/member/profile/login?continueUrl=https://www.nike.com/ca/")
    return driver

def clean_text(text):
    """Extract only temperature from text"""
    output = text.split(": ")
    return float(output[1])

def main():
    driver = get_driver()
    driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div/div[6]/form/div[2]/input").send_keys("Daps-o@live.com")
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div/div[6]/form/div[3]/input").send_keys("Owolabi93" + Keys.RETURN)
    time.sleep(2)
    #driver.find_element(By.XPATH,'/html/body/nav/div/a').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/footer/div/div[1]/div[1]/div/div[2]/div/ul/li[6]/a').click()
    time.sleep(2)
    
  
"""/html/body/div[5]/div/div/footer/div/div[1]/div[1]/div/div[2]/div/ul/li[6]/a"""

main()