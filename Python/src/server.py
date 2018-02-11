#!/usr/bin/env python3

from flask import Flask, request
from user import User
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.Table('Users')

def getFromDB(phoneNum):
    try:
    esponse = table.get_item(
            Key={
                'phoneNum': phoneNum,
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
    else:
        item = response['Item']
        return json.dumps(item, indent=4, cls=DecimalEncoder)

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    name = request.args.get("name")
    return "Hello %s!" % name

@app.route("/api/register")
def register():
    name = request.args.get("name")
    imgURL = request.args.get("imgURL")
    location = request.args.get("location")
    phone = request.args.get("phone")
    provider = request.args.get("provider")
    usr = User(username, name, imgURL, location, phone,\
        provider, [])
    ## TODO: add (usr.id, usr.json) to database
    return usr.json

@app.route("/api/addcontact")
def addContact(myID, otherPhone):
    ## usr = (TODO: get yourself from database by ID)
    phone = request.args.get("phone")
    ## contact = (TODO: get user by contact from database)
    # usr.addContect(contact)
    # DATABASE[usr.id] = usr.json 


# @app.route("/api/set")

# @app.route("/api/register", )
# def register():
#   return User()

if __name__ == "__main__":
    app.run()