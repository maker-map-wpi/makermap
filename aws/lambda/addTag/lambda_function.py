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


def addTool(id, type, tagID, tag):
    sql_cmd = ("INSERT INTO Labs(idTags, TagType, TagID, Tag) VALUES (%s, %s, %s, %s)")
    data = (id, type, tagID, tag)
    cursor.execute(sql_cmd, data)
    mydb.commit()