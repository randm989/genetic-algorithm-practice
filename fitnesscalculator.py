from individual import Individual
from attribute import Attribute

class FitnessCalculator:
	def __init__(self):
		self.solution = [.2, 0, 0, .9, -.3, 0, 0, 0]

	def getSolution(self):
		return self.solution

	def getFitness(self, ind):
		dist = 0
		for index in xrange(len(ind.attributeVector)):
			diff = ind.attributeVector[index] - self.solution[index]
			dist += diff * diff / len(ind.attributeVector)
				
		return 1 - dist

	def maxFitness(self):
		return 1