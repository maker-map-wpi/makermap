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


def addTool(type, tagID, tag):
    sql_cmd = ("INSERT INTO Labs(idTags, TaggedObjTable, TaggedObjID, Tag) VALUES (%s, %s, %s, %s)")
    data = (str(uuid.uuid4()), type, tagID, tag)
    cursor.execute(sql_cmd, data)
    mydb.commit()