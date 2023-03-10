import requests
newsapi_key = '559b300d693f4b779ec1395d142909cb'
#newsapi_link =f'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-2-27&to=2023-2-28&sortBy=popularity&language=en&apiKey={newsapi_key}'

# cmd + / to highlight and comment
#The %20 stands for space 
# 

# r = requests.get(newsapi_link)

# content = r.json()

# articles = content['articles']

# for article in articles:
#     print('Title\n', article['title'], '\nDescription\n', article['description'])

# print('\n',content['articles'][0].keys())

def get_news(topic, from_date, to_date, lang='en', api_key=newsapi_key):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={lang}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"Title\n {article['title']}, '\nDescription\n'{article['description']}")
    
    return results

macbooknews = get_news(topic='macbook', from_date='2023-02-10', to_date='2023-02-18')
print(macbooknews[1])