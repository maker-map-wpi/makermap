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
    sql_cmd = ('UPDATE Buildings SET Name = %s, Address = %s, Latitude = %s, Longitude = %s, Description = %s, ImageFolder = %s, Manager = %s, Hours = %s WHERE idBuildings = %s')
    data = (name, addr, lat, longi, desc, img, man, hour, idB)
    cursor.execute(sql_cmd, data)
    mydb.commit()
