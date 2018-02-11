#!/usr/bin/env python3

from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import smtplib
from message import Message
import json

class User(object):

    def __init__(self, name, imgURL,\
     location, phone, provider, contacts,\
     textstr="I need some help"):
        self.name = name
        self.imgURL = imgURL
        self.location = location
        self.phone = phone
        self.textstr = textstr
        self.contacts = contacts # list of Users
        self.provider = provider

    def __repr__(self):
        string = "User: %s" % self.name
        string += "\n\timage: %s" % self.imgURL
        string += "\n\tlocation: (%s, %s)" % (self.location[0], self.location[1])
        string += "\n\tphone: %s" % self.phone
        string += "\n\ttextstr: %s" % self.textstr
        string += "\n\tmessage: %s" % self.message
        string += "\n\temail: %s" % self.email
        string += ("\n***\nCONTACTS:\n***\n")
        for c in self.contacts:
            string += "\t\t%s\n" % c
        return string

    @property
    def email(self):
        if self.provider == "ATT":
            return self.phone + "@mms.att.net"
        elif self.provider == "Verizon":
            return self.phone + "@vtext.com"
            # TODO
        return None

    @property    
    def message(self):
        string = "%s\nI'm at %s" % \
         (self.textstr, self.address)
        return string

    @property
    def address(self):
        geolocator = Nominatim()
        location = geolocator.reverse(self.location)
        return location.address

    @property
    def json(self):
        cs = []
        for c in self.contacts:
            cs.append(c)
        usrDict = {
         "name": self.name, \
         "imgURL": self.imgURL, \
         "location": self.location, \
         "phone": self.phone, \
         "provider": self.provider, \
         "contacts": cs}
        return json.dumps(usrDict)

    def getDistance(self, other):
        return vincenty(self.location, other.location)

    def sendMessage(self, recipient):
        fromaddr = "uncommonmania@gmail.com"
        toaddr = recipient.email
        body = self.message

        pwd = "poorvaja2018"
        
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(fromaddr, pwd)
        print(body)
        s.sendmail(fromaddr, toaddr, body)
        s.quit()
    
    def addContact(self, phone):
        if phone not in self.contacts:
            self.contacts.append(phone)

    def isClose(self, other):
        return abs(float(self.location[0]) - float(other.location[0])) < .001 \
         and abs(float(self.location[1]) - float(other.location[1])) < .001
7

if __name__ == '__main__':
    user1 = User("Angela", "/none", \
        ("52.509669", "13.376294"), "7135347983",\
         "AT&T", [])
    user2 = User("cho yin", "/none", \
        ("51.509669", "13.376294"), "0000000000", \
        "Verizon", [], textstr="pls help")
    user1.addContact(user2)
    print(user1.json)
