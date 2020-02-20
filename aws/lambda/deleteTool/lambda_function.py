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


def deleteTool(id):
    sql_cmd = ("DELETE FROM Tools WHERE idTools = %s")
    data = (id,)
    cursor.execute(sql_cmd, data)
    mydb.commit()