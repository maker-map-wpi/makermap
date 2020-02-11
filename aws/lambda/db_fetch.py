import boto3
import json
from decimal import Decimal
from botocore.exceptions import ClientError
import time

resource23 = 'arn:aws:rds:us-east-2:490881226898:db:makermap',
secret23 = 'arn:aws:secretsmanager:us-east-2:490881226898:secret:makermap-IvwSup',


client = boto3.client('rds-data', region_name = 'us-east-2')
sql_commands=["SELECT * FROM Buildings","SELECT * FROM Labs","SELECT * FROM Tools","SELECT * FROM Tags"]

Tid = client.begin_transaction(resourceArn = resource23, secretArn = secret23).transactionId

def lambda_handler(event, context):
    print("hallo you ugly poato")
    try:
        results = []
        for cmd in sql_commands:
            print(cmd)
            response = client.execute_statement(
                continueAfterTimeout = True,
                resourceArn = resource,
                secretArn = secret,
                sql=cmd
                # sql = "SELECT *",
                # transactionId = Tid
            )
            print(response)
            results.append(response)
        print(results)
    except Exception as e:
        return_error(400,'who knows', e)

    return {
        'statusCode': 200,
        'body': results
    }

def return_error(code, msg, body={}):
    return {
        'statusCode': code,
        'message': msg,
        'body': body
    }
