#!/usr/bin/env python3

class Message(object):
	"""docstring for Message"""
	def __init__(self, text):
		self.sender = sender
		self.text = text

	def __repr__(self):
		string = "%s\nI'm at %s" % \
		 (self.text, self.sender.getAddress())
		return string

if __name__ == '__main__':
	msg = Message("I need some help")
	print(msg)