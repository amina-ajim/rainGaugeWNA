import pymysql #pip3 install pymysql


#create a mysql connection
conn =pymysql.connect(database="weather_data_schema",user="landslide",password="amma@123",host="localhost")

#create a mysql cursor
cur=conn.cursor()

data = {"sl no":2,"id":2015,"DISTRICT":"KODAGU","TALUKNAME":"MADIKERI","HOBLINAME":"GALIBIDU","Day1":0.0}

#cur.execute("INSERT INTO dailyData(sl no,id, DISTRICT, TALUKNAME, HOBLINAME, Day1) VALUES(%(2)s,%(2015)s,%("KODAGU")s,%("MADIKERI")s,%("GALIBIDU")s,%(0.0)s);",data)

cur.execute("INSERT INTO `dailyData` (`sl no`, `id`, `DISTRICT`, `TALUKNAME`, `HOBLINAME`, `Day1`) VALUES (%(sl no)s,%(id)s,%(DISTRICT)s,%(TALUKNAME)s,%(HOBLINAME)s,%(Day1)s);",data)

conn.commit()
conn.close()
