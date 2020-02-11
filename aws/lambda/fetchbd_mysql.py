import mysql.connector

mydb = mysql.connector.connect(
  host="makermap.cbeezzrvvyp6.us-east-2.rds.amazonaws.com",
  user="admin",
  passwd="makermap",
  database="innodb"
)

mycursor = mydb.cursor()
myresult = {}
sql_commands=["SELECT * FROM Buildings","SELECT * FROM Labs","SELECT * FROM Tools","SELECT * FROM Tags"]
type = ["buildings", "labs", "tools", "tags"]
i = 0
for sql in sql_commands:
    myresult[type[i]] = {}
    mycursor.execute(sql)
    labels = mycursor.description
    data = mycursor.fetchall()
    for x in range(len(data[0])):
            myresult[type[i]][labels[x][0]] = data[0][x]
    i += 1
print(myresult)
