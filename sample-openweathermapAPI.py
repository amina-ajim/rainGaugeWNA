import requests

OPEN_WEATHER_MAP_API_KEY = "your key here"

x=yourlat (9.052)
y=yourlong (72.369)

exclude = "current,alerts,minutely"
api_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(x)+"&lon="+str(y)+"&exclude="+exclude+"&appid="+{OPEN_WEATHER_MAP_API_KEY}+"&units=metric"

response = requests.get(api_url)
print(response)
