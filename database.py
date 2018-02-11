from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb',region_name='us-east-2') 

table = dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'phoneNum',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'phoneNum',
            'AttributeType': 'N'
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)



#print("Table status:", table.table_status)

ID = "Test User"
#year = 2015



#table.delete()
