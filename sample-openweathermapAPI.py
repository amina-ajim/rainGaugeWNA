import requests

OPEN_WEATHER_MAP_API_KEY = "b0ca473301875d2a23b6634f62749c3c"

x=10.054
y=77.120

exclude = "current,alerts,minutely"
api_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(x)+"&lon="+str(y)+"&exclude="+exclude+"&appid="+{OPEN_WEATHER_MAP_API_KEY}+"&units=metric"

response = requests.get(api_url)
print(response)
