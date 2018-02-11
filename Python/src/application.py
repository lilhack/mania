#!/usr/bin/env python3
from flask import Flask, request
from user import User
import boto3
import json
import decimal
import os
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Users')

def getUsersFromFile(file):
    with open(file) as f:
        data = json.load(f)
    usrs = []
    for p in data:
        usr = User(p["name"], "none", p["location"], p["phone"], \
         p["provider"], p["contacts"])
        usrs.append(usr)
    return usrs

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
        if "Item" in response:
            usr = response['Item']
            return usr
        return None

def getUser(phoneNum):
    dbResponse = getFromDB(phoneNum)
    if dbResponse is None or "Item" not in dbResponse:
        return None
    usrDict = json.loads(dbResponse["Item"])
    name = usrDict["name"]
    imgURL = usrDict["imgURL"]
    location = usrDict["location"]
    phone = usrDict["phone"]
    provider = usrDict["provider"]
    contacts = usrDict["contacts"]
    usr = User(name, imgURL, location, phone, provider, contacts)
    return usr

def putToDB(user):
    usrJson = {
        'phoneNum': user.phone,
        'Item': user.json
    }
    response = table.put_item(Item=usrJson)

application = app = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def start():
    return "Hello World!"

@application.route("/api/hello", methods=['GET', 'POST'])
def hello():
    name = request.args.get("name")
    return "Hello %s!" % name

@application.route("/api/messageall", methods=['GET', 'POST'])
def messageAll():
    usrs = getUsersFromFile("database.json")
    usrs[0].sendMessage(usrs[1])
    return "ok"

@application.route("/api/getuser", methods=['GET', 'POST'])
def printUser():
    phoneNum = request.args.get("phonenum")
    usr = getUser(phoneNum)
    return usr.json

@application.route("/api/register", methods=['GET', 'POST'])
def register():
    name = request.args.get("name")
    imgURL = request.args.get("imgURL")
    lon = request.args.get("lon")
    lat = request.args.get("lat")
    location = (lat, lon)
    phone = request.args.get("phone")
    provider = request.args.get("provider")
    usr = User(name, imgURL, location, phone,\
        provider, [])
    putToDB(usr)
    return usr.json

@application.route("/api/addcontact", methods=['GET', 'POST'])
def addContact():
    phoneNum = request.args.get("myphone")
    usr = getUser(phoneNum)
    phone = request.args.get("otherphone")
    usr.addContact(phone)
    putToDB(usr) 
    return usr.json

@application.route("/api/messagecontacts", methods=['GET', 'POST'])
def messageContacts():
    phone = request.args.get("myphone")
    usr = getUser(phone)
    for num in usr.contacts:
        contact = getUser(num)
        if contact:
            usr.sendMessage(contact)
    return "ok"

@application.route("/api/messagelocal", methods=['GET', 'POST'])
def messageLocal():
    phone = request.args.get("myphone")
    me = getUser(phone)
    if not me:
        return "error: myphone not valid"
    response = table.scan(
        ProjectionExpression="phoneNum"
        )
    numsDictList = response["Items"]
    sent = ""
    for numDict in numsDictList:
        otherNum = numDict["phoneNum"]
        other = getUser(otherNum)
        if me.location[0] and me.location[1] and \
         other and other.location[0] and other.location[1] \
         and me.isClose(other) and (other.phone != me.phone):
            print(other.email)
            me.sendMessage(other)
            sent += other.name + "\n"
    return sent

if __name__ == "__main__":
    application.run()
