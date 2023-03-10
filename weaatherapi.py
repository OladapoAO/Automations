import requests
data = open('data.txt','x')
data.write('City, Time, Temperature, Condtion')
api_key = '62551a74425023512a82f051c46edb56'
city_name = 'Toronto'
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric'

r = requests.get(url)
content = r.json()
forecasts = content['list']

for forecast in forecasts:
    temp = forecast['main']['temp']
    time = forecast['dt_txt']
    condition = forecast['weather'][0]['description']

    data.write(f"\n{city_name},{time},{temp},{condition}")

# temp_dict = [{'city':'toronto', 'time':'15:30', 'temp':'0', 'condtion':'clouds'}, 
#              {'city':'toronto', 'time':'16:30', 'temp':'2', 'condtion':'cloudy'}]

# data = open('data.txt','x')
# data.write('City, Time, Temperature, Condtion')

# for temps in temp_dict:
#     data.write(f"\n{temps['city']},{temps['time']},{temps['temp']},{temps['condtion']}")