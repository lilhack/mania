#!/usr/bin/env python3

from user import User

class Message(object):
	"""docstring for Message"""
	def __init__(self, sender, text):
		self.sender = sender
		self.text = text

	def __repr__(self):
		string = "%s says: %s \nI'm at %s" % \
		 (self.sender.name, self.text, self.sender.getAddress())
		return string

if __name__ == '__main__':
	user1 = User("choyin1", "cho yin", "/none", ("52.509669", "13.376294"), "000-000-0000")
	msg = Message(user1, "I need some help")
	print(msg)