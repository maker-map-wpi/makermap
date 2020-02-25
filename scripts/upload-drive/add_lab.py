import mysql.connector
import json
import uuid

# connect to db
mydb = mysql.connector.connect(
  host="makermap.cbeezzrvvyp6.us-east-2.rds.amazonaws.com",
  user="admin",
  passwd="makermap",
  database="innodb"
)

cursor = mydb.cursor()


def addLab(idB, name, hour, lat, longi, desc, room, img, man):
    sql_cmd = ("INSERT INTO Labs(idLabs, BuildingID, Name, Hours, Latitude, Longitude, Description, RoomNum, ImageFolder, Manager) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data = (str(uuid.uuid4()), idB, name, hour, lat, longi, desc, room, img, man)
    cursor.execute(sql_cmd, data)
    mydb.commit()