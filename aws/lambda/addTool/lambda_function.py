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


def addTool(idT, name, idL, desc, img, book, own, res):
    sql_cmd = ("INSERT INTO Labs(idTools, Name, LabID, Description, ImageFolder, BookingLink, OwnerID, RestrictPublic) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    data = (idT, name, idL, desc, img, book, own, res)
    cursor.execute(sql_cmd, data)
    mydb.commit()