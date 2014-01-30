from individual import Individual
from fitnesscalculator import FitnessCalculator


class Population:

	fit = FitnessCalculator()

	def __init__(self, populationSize = 30, initialize = True):
		self.individuals = []

		if initialize:
			for i in xrange(populationSize):
				self.individuals += [Individual()]

	def size(self):
		return len(self.individuals)

	def addIndividual(self, ind):
		self.individuals += [ind]

	def getFittest(self):
		result = self.individuals[0]
		maxFit = Population.fit.getFitness(result)
		for ind in self.individuals:
			newFit = Population.fit.getFitness(ind)
			if maxFit > newFit:
				result = ind
				maxFit = newFit
		return result

	def averageFitness(self):
		result = 0.0
		for ind in self.individuals:
			result += Population.fit.getFitness(ind)
			
		return result / len(self.individuals)

	def __str__(self):
		#for ind in self.individuals:
		#	print str(ind) + " " + str(Population.fit.getFitness(ind))
		#return "Pop size: " + str(len(self.individuals))
		return ""


if __name__ == "__main__":
	pop = Population()
	print pop