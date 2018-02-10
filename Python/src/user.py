#!/usr/bin/env python3
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

class User(object):

    def __init__(self, username, name, imgURL, location, phone, contacts, text="I need some help"):
        self.username = username
        self.name = name
        self.imgURL = imgURL
        self.location = location
        self.phone = phone
        self.text = text
        self.contacts = contacts # list of Users

    def __repr__(self):
        string = "User: %s" % self.username
        string += "\n\timage: %s" % self.imgURL
        string += "\n\tlocation: (%s, %s)" % (self.location[0], self.location[1])
        string += "\n\tphone: %s" % self.phone
        string += "\n\ttext: %s" % self.text
        string += ("***\nCONTACTS:\n***\n")
        for c in self.contacts:
            string += str(c)
        return string

    def getAddress(self):
        geolocator = Nominatim()
        location = geolocator.reverse(self.location)
        return location.address

    def getDistance(self, other):
        return vincenty(self.location, other.location)

    def sendMessage(self, recipient):
        message = Message(self, self.text)
        recipient.notify(message)

    def addContact(self, contact):
        self.contacts.append(contact)

    def notify(self, message):
        pass

if __name__ == '__main__':
    user1 = User("choyin1", "cho yin", "/none", ("52.509669", "13.376294"), "0000000000", [])
    print(user1.getAddress())
    user2 = User("choyin2", "cho yin", "/none", ("51.509669", "13.376294"), "0000000000", [], text="pls help")
    print(user1.getDistance(user2))
    user2.addContact(user1)
    print(user2)