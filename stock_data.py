import requests

url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1677196800&interval=1d&events=history&includeAdjustedClose=true"


content = requests.get(url).content

print(content)