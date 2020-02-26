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


def editTool(idT, name, idL, desc, img, book, own, res):
    sql_cmd = ("UPDATE Tools SET name = %s, labID = %s, description = %s, imageFolder = %s, bookingLink = %s, ownerID = %s, restrictPublic = %s WHERE idTools = %s")
    data = (name, idL, desc, img, book, own, res, idT)
    cursor.execute(sql_cmd, data)
    mydb.commit()