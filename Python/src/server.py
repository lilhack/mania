#!/usr/bin/env python3

from flask import Flask, request
from user import User

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    name = request.args.get("name")
    return "Hello %s!" % name

@app.route("/api/register")
def register():
    username = request.args.get("username")
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