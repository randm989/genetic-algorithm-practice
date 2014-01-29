import random

class Attribute:
	def __init__(self, value = -1):
		if value == -1:
			self.randomInit()
		else:
			self.value = value

	def setValue(self, value):
		self.value = value

	def randomInit(self):
		self.value = random.uniform(0,100)

	def __str__(self):
		return str(self.value)