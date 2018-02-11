
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb',region_name='us-east-2')


ID = "Test User"
phoneNum = "4083355866"

table = dynamodb.Table('Users')
response = table.put_item(
   TableName="Users",
   Item={
        'phoneNum': phoneNum,
        'ID':ID,
       # 'title': title,
        'info': {
            'plot':"Nothing happens at all.",
            'rating': "meh"
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4))
