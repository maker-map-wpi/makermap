import mysql.connector
import json


def lambda_handler(event, context):

    output=get_data()

    return {
        'statusCode': 200,
        'body': output
    }

def return_error(code, msg, body={}):
    return {
        'statusCode': code,
        'message': msg,
        'body': body
    }






def get_data():
    # connect to db
    mydb = mysql.connector.connect(
      host="makermap.cbeezzrvvyp6.us-east-2.rds.amazonaws.com",
      user="admin",
      passwd="makermap",
      database="innodb"
    )

    # init vars
    mycursor = mydb.cursor()
    myresult = {}
    sql_commands=["SELECT * FROM Buildings","SELECT * FROM Labs","SELECT * FROM Tools","SELECT * FROM Tags"]
    type = ["Buildings", "Labs", "Tools", "Tags"]
    i = 0

    # fetch all the data
    for sql in sql_commands:
        myresult[type[i]] = {}
        mycursor.execute(sql)
        labels = mycursor.description
        data = mycursor.fetchall()

        # convert data to dict
        for row in range(len(data)):
            myresult[type[i]][data[row][1]] = {}
            for col in range(len(data[row])):
              myresult[type[i]][data[row][1]][labels[col][0]] = data[row][col]
        i += 1
    # add tags
    for tag in myresult["Tags"]:
      if myresult["Tags"][tag]["TagType"] == "Tools":
        for tool in myresult["Tools"]:
          if myresult["Tools"][tool]["idTools"] == myresult["Tags"][tag]["TaggedObjID"]:
            myresult["Tools"][tool]["Tags"] = {}
            myresult["Tools"][tool]["Tags"][myresult["Tags"][tag]["Tag"]] = myresult["Tags"][tag]


      elif myresult["Tags"][tag]["TagType"] == "Labs":
        for lab in myresult["Labs"]:
          if myresult["Labs"][lab]["idLabs"] == myresult["Tags"][tag]["TaggedObjID"]:
            myresult["Labs"][lab]["Tags"] = {}
            myresult["Labs"][lab]["Tags"][myresult["Tags"][tag]["Tag"]] = myresult["Tags"][tag]

      elif myresult["Tags"][tag]["TagType"] == "Buildings":
       for building in myresult["Buildings"]:
          if myresult["Buildings"][building]["idBuildings"] == myresult["Tags"][tag]["TaggedObjID"]:
            myresult["Buildings"][building]["Tags"] = {}
            myresult["Buildings"][building]["Tags"][myresult["Tags"][tag]["Tag"]] = myresult["Tags"][tag]

    # add tools to their labs
    for lab in myresult["Labs"]:
        myresult["Labs"][lab]["Tools"] = {}
        for tool in myresult["Tools"]:
            if myresult["Tools"][tool]["LabID"] == myresult["Labs"][lab]["idLabs"]:
                myresult["Labs"][lab]["Tools"][myresult["Tools"][tool]["Name"]] = (myresult["Tools"][tool])

    # add labs to their buildings
    for building in myresult["Buildings"]:
        myresult["Buildings"][building]["Labs"] = {}
        for lab in myresult["Labs"]:
            if myresult["Labs"][lab]["BuildingID"] == myresult["Buildings"][building]["idBuildings"]:
                myresult["Buildings"][building]["Labs"][myresult["Labs"][lab]["Name"]] = (myresult["Labs"][lab])

    # convert from dict to json
    return json.dumps(myresult["Buildings"])

print(get_data())
