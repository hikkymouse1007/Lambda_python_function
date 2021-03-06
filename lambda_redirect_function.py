import json
import boto3
from datetime import datetime
 
s3 = boto3.resource('s3')      # ③S3オブジェクトを取得
 
# ④Lambdaのメイン関数
def lambda_handler(event, context):
    bucket = 'your-bucket-name'    # ⑤バケット名を指定
    key = 'test_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.txt'  # ⑥オブジェクトのキー情報を指定
    file_contents = 'Lambda test'  # ⑦ファイルの内容
    
    obj = s3.Object(bucket,key)     # ⑧バケット名とパスを指定
    obj.put( Body=file_contents )   # ⑨バケットにファイルを出力
    response = {
        'status': '302',CORS
        'statusDescription': 'Found',
        'headers': {
            'location': [{
                'key': 'Location',
                'value': 'http://xxxxx.cloudfront.net/1x1.gif'
            }]
        }
    }
    return response