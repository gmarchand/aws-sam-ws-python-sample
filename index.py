import json
import datetime
import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')

# List all items of the DynamoDB Table
def list(event, context):
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    result = table.scan()
    data = {
        'output': 'Hello World List',
        'body': json.dumps(result['Items']),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}


# Get an item from the DynamoDB table
def get(event,context):
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    name = event['pathParameters']['name']

    # fetch todo from the database
    result = table.get_item(
        Key={
            'name': name
        }
    )

    data = {
        'output': 'Hello World Get',
        'body' : result['Item'],
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
        'body' : result,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}