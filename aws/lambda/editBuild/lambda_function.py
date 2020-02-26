import mysql.connector
import json

# connect to db
mydb = mysql.connector.connect(
  host="makermap.cbeezzrvvyp6.us-east-2.rds.amazonaws.com",
  user="admin",
  passwd="makermap",
  database="innodb"
)

cursor = mydb.cursor()

def editBuilding(idB, name, addr, lat, longi, desc, img, man, hour):
    sql_cmd = ('UPDATE Buildings SET name = %s, address = %s, latitude = %s, longitude = %s, description = %s, imageFolder = %s, manager = %s, hours = %s WHERE idBuildings = %s')
    data = (name, addr, lat, longi, desc, img, man, hour, idB)
    cursor.execute(sql_cmd, data)
    mydb.commit()
