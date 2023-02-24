import requests
from datetime import datetime
import time

from_date = input('Enter Start Date in yyyy/mm/dd format: ')
from_datetime = datetime.strptime(from_date,'%Y/%m/%d')
from_epoch = int( time.mktime(from_datetime.timetuple()) )

to_date = input('Enter End Date in yyyy/mm/dd format: ')
to_datetime = datetime.strptime(to_date,'%Y/%m/%d') 
to_epoch = int( time.mktime(to_datetime.timetuple()) )

ticker = input('What stock data do you want? ')


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content

#content = str(content)
#print(content)

def stock_to_csv(content, ticker):
    filename = f"{ticker}.csv"

    with open(filename,'wb') as file:
        file.write(content)


stock_to_csv(content,ticker)