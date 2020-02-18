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


def addBuilding(idB, name, addr, lat, longi, desc, img, man, hour):
    sql_cmd = ("INSERT INTO Buildings(idBuildings, Name, Address, Latitude, Longitude, Description, ImageFolder, Manager, Hours) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (idB, name, addr, lat, longi, desc, img, man, hour)
    cursor.execute(sql_cmd, data)
    mydb.commit()