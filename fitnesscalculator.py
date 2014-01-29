from individual import Individual
from attribute import Attribute

class FitnessCalculator:
	def __init__(self):
		self.solution = [Attribute(23), Attribute(76)]

	def getSolution(self):
		return self.solution

	def getFitness(self, ind):
		xdiff = ind.attributes[0].value - self.solution[0].value
		ydiff = ind.attributes[1].value - self.solution[1].value
		dist = xdiff * xdiff + ydiff * ydiff
				
		return 100 * 100 - dist

	def maxFitness(self):
		return 100 * 100