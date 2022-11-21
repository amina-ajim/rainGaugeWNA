import pymysql #pip3 install pymysql
import requests

#create a mysql connection
conn =pymysql.connect(database="weather_data_schema",user="landslide",password="amma@123",host="localhost")

OPEN_WEATHER_MAP_API_KEY = "b0ca473301875d2a23b6634f62749c3c"

x=10.054
y=77.120

api_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(x)+"&lon="+str(y)+"&appid=b0ca473301875d2a23b6634f62749c3c&units=metric&exclude=hourly,daily,alerts,minutely"

response = requests.get(api_url)
data = response.content
print(type(data))
current =  data["current"]


apiData = {"latitude":data[lat],"longitude":data[lon],"temp":current[temp],"wspd":current[wind_speed],"wgust":current[wind_gust],"pressure":current[pressure]}

#create a mysql cursor
cur=conn.cursor()

#data = {"sl no":2,"id":2015,"DISTRICT":"KODAGU","TALUKNAME":"MADIKERI","HOBLINAME":"GALIBIDU","Day1":0.0}

#cur.execute("INSERT INTO dailyData(sl no,id, DISTRICT, TALUKNAME, HOBLINAME, Day1) VALUES(%(2)s,%(2015)s,%("KODAGU")s,%("MADIKERI")s,%("GALIBIDU")s,%(0.0)s);",data)

cur.execute("INSERT INTO `weather_data` (`latitude`, `longitude`, `temp`, `wspd`, `wgust`, 'pressure') VALUES (%(lat)s,%(lon)s,%(temp)s,%(wind_speed)s,%(wind_gust)s,%(pressure)s);",apiData)

conn.commit()
conn.close()








