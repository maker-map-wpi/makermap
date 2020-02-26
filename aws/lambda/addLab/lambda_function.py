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
    sql_cmd = ("INSERT INTO Labs(idLabs, buildingID, name, hours, latitude, longitude, description, roomNum, imageFolder, manager) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data = (str(uuid.uuid4()), idB, name, hour, lat, longi, desc, room, img, man)
    cursor.execute(sql_cmd, data)
    mydb.commit()