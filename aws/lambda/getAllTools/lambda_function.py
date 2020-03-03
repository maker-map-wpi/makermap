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
    type = ["buildings", "labs", "tools", "tags"]
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
    for tag in myresult["tags"]:
      if myresult["tags"][tag]["taggedObjTable"] == "tools":
        for tool in myresult["tools"]:
          if myresult["tools"][tool]["idTools"] == myresult["tags"][tag]["taggedObjID"]:
            myresult["tools"][tool]["tags"] = {}
            myresult["tools"][tool]["tags"][myresult["tags"][tag]["Tag"]] = myresult["tags"][tag]


      elif myresult["tags"][tag]["taggedObjTable"] == "labs":
        for lab in myresult["labs"]:
          if myresult["labs"][lab]["idLabs"] == myresult["tags"][tag]["taggedObjID"]:
            myresult["labs"][lab]["tags"] = {}
            myresult["labs"][lab]["tags"][myresult["tags"][tag]["Tag"]] = myresult["tags"][tag]

      elif myresult["tags"][tag]["taggedObjTable"] == "buildings":
       for building in myresult["buildings"]:
          if myresult["buildings"][building]["idBuildings"] == myresult["tags"][tag]["taggedObjID"]:
            myresult["buildings"][building]["tags"] = {}
            myresult["buildings"][building]["tags"][myresult["tags"][tag]["Tag"]] = myresult["tags"][tag]

    # add tools to their labs
    for lab in myresult["labs"]:
        myresult["labs"][lab]["tools"] = {}
        for tool in myresult["tools"]:
            if myresult["tools"][tool]["labID"] == myresult["labs"][lab]["idLabs"]:
                myresult["labs"][lab]["tools"][myresult["tools"][tool]["name"]] = (myresult["tools"][tool])

    # add labs to their buildings
    for building in myresult["buildings"]:
        myresult["buildings"][building]["labs"] = {}
        for lab in myresult["labs"]:
            if myresult["labs"][lab]["buildingID"] == myresult["buildings"][building]["idBuildings"]:
                myresult["buildings"][building]["labs"][myresult["labs"][lab]["name"]] = (myresult["labs"][lab])
    
    r = [v for v in myresult['buildings'].values()]
    # convert from dict to json
    return json.dumps(r)

