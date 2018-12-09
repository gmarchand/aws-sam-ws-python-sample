import json
import datetime
import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
    name = event['pathParameters']['name']
    
    logger.info('Hello %s !', name)
    
    result = table.put_item(
        Item = {
                'name': name,
                'timestamp': datetime.datetime.utcnow().isoformat()
               } 
        )

    logger.info(result)
    
    data = {
        'output': 'Hello World Post',
        'body' : event,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(result),
            'headers': {'Content-Type': 'application/json'}}