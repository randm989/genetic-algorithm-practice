from attribute import Attribute
import random

class Individual:
	numAtts = 8
	def __init__(self, init = True):
		self.attributeVector = []
		if init:
			for i in xrange(Individual.numAtts):
				self.attributeVector += [random.random() * 2 - 1]

	def description(self):
		result = ""
		for att in self.attributeVector:
			result += str(att) + " "
		return result

	def __getitem__(self, index):
		return self.attributeVector[index]

	def __str__(self):
		return self.description()

	def __repr__(self):
		return self.description()