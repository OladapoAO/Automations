import requests
newsapi_key = 'get from api notebook'

def get_news(country, api_key=newsapi_key):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"Title\n {article['title']}, '\nDescription\n'{article['description']}")
    
    return results

macbooknews = get_news(country='us')
print(macbooknews[1])