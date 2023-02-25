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
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver

def clean_text(text):
    """Extract only temperature from text"""
    output = text.split(": ")
    return float(output[1])

def main():
    driver = get_driver()
    time.sleep(3)
    element = driver.find_element(By.XPATH,'//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
    element = element.text
    element = element[0:5]
    stock_percentage = float(element)

    return (stock_percentage, type(stock_percentage))

stock_percentage = main()
stock_percentage = stock_percentage[0]

def send_email(stock):
    if stock < -0.10 :
        print(f'send email - Stock CROBEX is less than 0.10% @ {stock}')
    else:
        print(f'Stock CROBEX is at {stock}')

send_email(stock_percentage)