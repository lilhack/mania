#!/usr/bin/env python3

class User(object):

	def __init__(self, username, imgURL, location, phone):
		self.username = username
		self.imgURL = imgURL
		self.location = location
		self.phone = phone

	def __repr__(self):
		string = "User: %s" % self.username
		string += "\n\timage: %s" % self.imgURL
		string += "\n\tlocation: (%f, %f)" % (self.location[0], self.location[1])
		string += "\n\tphone: %s" % self.phone
		return string

if __name__ == '__main__':
	user1 = User("choyin", "/none", (1,2), "000-000-0000")
	print(user1)