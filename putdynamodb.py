import boto3
import json

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('timestampdb')
from datetime import datetime

def lambda_handler(event, context):
    table_name = 'timestampdb'
    item = {
        "timestamp": {"S": datetime.now().strftime('%Y-%m-%d-%H:%M:%S')},
        "name"     : {"S": "test"}
    }

    dynamo = boto3.client('dynamodb')
    dynamo.put_item(TableName=table_name, Item=item)
    return 