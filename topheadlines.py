import requests
newsapi_key = '559b300d693f4b779ec1395d142909cb'

def get_news(country, api_key=newsapi_key):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"Title\n {article['title']}, '\nDescription\n'{article['description']}")
    
    return results

macbooknews = get_news(topic='macbook', from_date='2023-02-10', to_date='2023-02-18')
print(macbooknews[1])