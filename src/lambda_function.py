```python
import json
import boto3
import uuid
from boto3.dynamodb.conditions import Key

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# DynamoDB table name
table = dynamodb.Table('users-table')


def lambda_handler(event, context):

    http_method = event['httpMethod']

    # CREATE USER
    if http_method == 'POST':

        body = json.loads(event['body'])

        user_id = str(uuid.uuid4())

        item = {
            'userId': user_id,
            'name': body['name'],
            'role': body['role']
        }

        table.put_item(Item=item)

        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'User created successfully',
                'data': item
            })
        }

    # READ USER
    elif http_method == 'GET':

        user_id = event['pathParameters']['id']

        response = table.get_item(
            Key={
                'userId': user_id
            }
        )

        item = response.get('Item')

        if item:

            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }

        else:

            return {
                'statusCode': 404,
                'body': json.dumps({
                    'message': 'User not found'
                })
            }

    # UPDATE USER
    elif http_method == 'PUT':

        user_id = event['pathParameters']['id']

        body = json.loads(event['body'])

        response = table.update_item(
            Key={
                'userId': user_id
            },
            UpdateExpression='SET #n = :name, #r = :role',
            ExpressionAttributeNames={
                '#n': 'name',
                '#r': 'role'
            },
            ExpressionAttributeValues={
                ':name': body['name'],
                ':role': body['role']
            },
            ReturnValues='UPDATED_NEW'
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'User updated successfully',
                'updatedAttributes': response['Attributes']
            })
        }

    # DELETE USER
    elif http_method == 'DELETE':

        user_id = event['pathParameters']['id']

        table.delete_item(
            Key={
                'userId': user_id
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'User deleted successfully'
            })
        }

    # INVALID METHOD
    else:

        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Invalid HTTP method'
            })
        }
```
