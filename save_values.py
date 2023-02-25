from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """Extract only temperature from text"""
    output = text.split(": ")
    return float(output[1])

def write_file(text):
    """ Write input text into a text file"""
    filename = f"{datetime.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename,'w') as file:
        file.write(text)

def main():
    driver = get_driver()
    while True:
        time.sleep(2)
        element = driver.find_element(By.XPATH,"/html/body/div/div/h1[2]")
        text = str(clean_text(element.text))
        write_file(text)

  

print(main())