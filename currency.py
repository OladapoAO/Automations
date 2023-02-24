from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency, amount=1):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}'
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(rate[:-4])
    
    return rate

current_rate = get_currency('GBP','AUD')

print(current_rate)