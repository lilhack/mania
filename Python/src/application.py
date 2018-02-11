#!/usr/bin/env python3

from flask import Flask, request
from user import User
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def getUsersFromFile(file):
    with open(file) as f:
        data = json.load(f)
    usrs = []
    for p in data:
        usr = User(p["name"], "none", p["location"], p["phone"], \
         p["provider"], p["contacts"])
        usrs.append(usr)
    return usrs

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

if __name__ == "__main__":
    application.run()
