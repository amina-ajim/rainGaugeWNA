import pymysql #pip3 install pymysql


#create a mysql connection
conn =pymysql.connect(database="databseName",user="UN",password="PWD",host="localhost")

#create a mysql cursor
cur=conn.cursor()

data = {"field1data":value,"field2data":value,"fieldndata":value}

cur.execute("INSERT INTO tableName(field1, field2,.... fieldn) VALUES(%(field1data)s,%(field2data)s,%(field3data)s);",data)

conn.commit()
conn.close()
