import json
import datetime
import boto3
import os

dynamodb = boto3.resource('dynamodb')

# List all items of the DynamoDB Table
def get(event, context):
    print(os.environ)
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    result = table.scan()
    data = {
        'output': 'Hello World Get',
        'body': json.dumps(result['Items']),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

# Post a new Item to the DynamoDB table
def post(event, context):
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    data = {
        'output': 'Hello World Post',
        'body' : event,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}