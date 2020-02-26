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

def editLab(idL, idB, name, hour, lat, longi, desc, room, img, man):
    sql_cmd = ("UPDATE Labs SET buildingID = %s, name = %s, hours = %s, latitude = %s, longitude = %s, description = %s, roomNum = %s, imageFolder = %s, manager = %s WHERE idLabs = %s")
    data = (idB, name, hour, lat, longi, desc, room, img, man, idL)
    cursor.execute(sql_cmd, data)
    mydb.commit()
