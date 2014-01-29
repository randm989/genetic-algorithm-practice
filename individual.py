from attribute import Attribute

class Individual:
	numAtts = 2
	def __init__(self, init = True):
		self.attributes = []
		if init:
			for i in xrange(Individual.numAtts):
				self.attributes += [Attribute()]

	def description(self):
		result = ""
		for att in self.attributes:
			result += str(att.value) + " "
		return result

	def __getitem__(self, index):
		return self.attributes[index]

	def __str__(self):
		return self.description()

	def __repr__(self):
		return self.description()