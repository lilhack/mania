#!/usr/bin/env python3

from flask import Flask, request
from user import User
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Users')

def getFromDB(phoneNum):
    try:
        response = table.get_item(
            Key={
                'phoneNum': phoneNum,
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
    else:
        usr = response['Item']
        return usr

def putToDB(user):
    usrJson = {
        'phoneNum': user.phoneNum,
        'info': user.json
    }
    response = table.put_item(usrJson)

application = Flask(__name__)

@application.route("/api/hello")
def hello():
    name = request.args.get("name")
    return "Hello %s!" % name

@application.route("/api/getuser")
def getUser():
    phoneNum = request.args.get("phonenum")
    usr = getFromDB(phoneNum)
    return json.dumps(usr, indent=4)

@application.route("/api/register")
def register():
    name = request.args.get("name")
    imgURL = request.args.get("imgURL")
    location = request.args.get("location")
    phone = request.args.get("phone")
    provider = request.args.get("provider")
    usr = User(name, imgURL, location, phone,\
        provider, [])
    putToDB(usr)
    return usr.json

@application.route("/api/addcontact")
def addContact(myID, otherPhone):
    ## usr = (TODO: get yourself from database by ID)
    phone = request.args.get("phone")
    ## contact = (TODO: get user by contact from database)
    # usr.addContect(contact)
    # DATABASE[usr.id] = usr.json 

if __name__ == "__main__":
    application.run()