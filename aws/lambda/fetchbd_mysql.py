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
type = ["Buildings", "Labs", "Tools", "Tags"]
i = 0
for sql in sql_commands:
    myresult[type[i]] = {}
    mycursor.execute(sql)
    labels = mycursor.description
    data = mycursor.fetchall()
    for row in range(len(data)):
        myresult[type[i]][row] = {}
        for col in range(len(data[row])):
                myresult[type[i]][row][labels[col][0]] = data[row][col]
    i += 1
print(myresult["Buildings"][0]["Description"])

for lab in myresult["Labs"]:
    myresult["Labs"][lab]["Tools"] = []
    for tool in myresult["Tools"]:
        if myresult["Tools"][tool]["LabID"] == myresult["Labs"][lab]["idLabs"]:
            myresult["Labs"][lab]["Tools"].append(myresult["Tools"][tool])
# print(myresult["Labs"][0])

for building in myresult["Buildings"]:
    myresult["Buildings"][building]["Labs"] = []
    for lab in myresult["Labs"]:
        if myresult["Labs"][lab]["BuildingID"] == myresult["Buildings"][building]["idBuildings"]:
            myresult["Buildings"][building]["Labs"].append(myresult["Labs"][lab])
# print(myresult["Buildings"][0])



# attempting to link with sql commands
# sql = SELECT * FROM Buildings INNER JOIN Labs ON Buildings.Labs = Labs.BuildingID
# myresult[type[i]] = {}
# mycursor.execute(sql)
# labels = mycursor.description
# data = mycursor.fetchall()
# for x in range(len(data[0])):
#         myresult[type[i]][labels[x][0]] = data[0][x]
