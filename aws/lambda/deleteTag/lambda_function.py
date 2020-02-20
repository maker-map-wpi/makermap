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


def deleteTag(id):
    sql_cmd = ("DELETE FROM Tags WHERE idTag = %s")
    data = (id,)
    cursor.execute(sql_cmd, data)
    mydb.commit()