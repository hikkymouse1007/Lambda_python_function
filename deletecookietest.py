import boto3
import json

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('cookieDB')

def lambda_handler(event, context):
    # APIからクエリ文字をパラメータとして受け取る
    cookie_id = event.get('queryStringParameters').get('cookie_id')
    # ソートキーを設定していない場合はプライマリーキーのみ指定
    response = table.delete_item(
        Key={
            'cookie_id': cookie_id,
        }
    )
    # CORSの必須パラメータ(headers)
    return {
        'statusCode': 200,
        'body': json.dumps("Data deleted!"),
        'headers': {
          'Content-Type': 'application/json', 
          "Access-Control-Allow-Origin": "*"
        },
    }