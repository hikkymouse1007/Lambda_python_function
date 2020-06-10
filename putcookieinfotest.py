import boto3
import json

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('cookieDB')

def lambda_handler(event, context):
    # cookie_idはstring型
    cookie_id = event.get('queryStringParameters').get('cookie_id')
    table_name = 'cookieDB'
    item = {
       "cookie_id": {"S": cookie_id},
       "name"     : {"S": "hello"},
    }
    dynamo = boto3.client('dynamodb')
    putResponse = dynamo.put_item(TableName=table_name, Item=item)
    # プロキシ統合レスポンス必須パラメータ
    return {
        'statusCode': 200,
        'body': json.dumps("Data added!"),
        'headers': {
          'Content-Type': 'application/json', 
          "Access-Control-Allow-Origin": "*"
        },
    }