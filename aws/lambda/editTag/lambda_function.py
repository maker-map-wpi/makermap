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


def editTag(idT,tType, tagID, tag):
    sql_cmd = ("UPDATE Labs SET taggedObjTable = %s, taggedObjID = %s, tag = %s WHERE idTags = %s")
    data = (tType, tagID, tag, idT)
    cursor.execute(sql_cmd, data)
    mydb.commit()