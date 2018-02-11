#!/usr/bin/env python3
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import smtplib
from email.message import EmailMessage
from message import Message

class User(object):

    def __init__(self, username, name, imgURL, location, phone, provider, contacts, textstr="I need some help"):
        self.username = username
        self.name = name
        self.imgURL = imgURL
        self.location = location
        self.phone = phone
        self.textstr = textstr
        self.contacts = contacts # list of Users
        self.provider = provider

    def __repr__(self):
        string = "User: %s" % self.username
        string += "\n\timage: %s" % self.imgURL
        string += "\n\tlocation: (%s, %s)" % (self.location[0], self.location[1])
        string += "\n\tphone: %s" % self.phone
        string += "\n\ttextstr: %s" % self.textstr
        string += "\n\tmessage: %s" % self.message
        string += "\n\temail: %s" % self.email
        string += ("\n***\nCONTACTS:\n***\n")
        for c in self.contacts:
            string += str(c)
        return string

    @property
    def email(self):
        if self.provider == "AT&T":
            return self.phone + "@mms.att.net"
        elif self.provider == "Verizon":
            pass
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

    def getDistance(self, other):
        return vincenty(self.location, other.location)

    
    def addContact(self, contact):
        self.contacts.append(contact)


if __name__ == '__main__':
    user1 = User("angela1", "Angela", "/none", \
        ("52.509669", "13.376294"), "7135347983",\
         "AT&T", [])
    user2 = User("choyin2", "cho yin", "/none", \
        ("51.509669", "13.376294"), "0000000000", \
        "Verizon", [], textstr="pls help")
    print(user1)