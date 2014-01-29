from population import Population
from individual import Individual
from attribute import Attribute
import random

class Breeder:
	uniformRate = 0.5
	mutationRate = 0.1
	tourneySize = 5
	elitism = False
	
	def __init__(self, population):
		self.pop = population

	def evolve(self):
		newPop = Population(self.pop.size(), False)

		i = 0
		while i < self.pop.size():
			ind1 = self.tourney()
			ind2 = self.tourney()
			newInd = self.breed(ind1, ind2)
			newPop.addIndividual(newInd)
			i += 1

		return newPop

	def breed(self, ind1, ind2):
		newInd = Individual(False)

		for i in xrange(Individual.numAtts):
			parentInd = None
			if random.random() > Breeder.uniformRate:
				parentInd = ind1
			else:
				parentInd = ind2
			newVal = parentInd[i].value
			newInd.attributes += [Attribute(newVal)]

		self.mutate(newInd)

		return newInd


	def mutate(self, ind):
		for i in ind.attributes:
			if random.random() < Breeder.mutationRate:
				i.value += (random.random() * 2 - 1) * (Population.fit.maxFitness() - Population.fit.getFitness(ind))

	def tourney(self):
		tourneyPop = Population(Breeder.tourneySize, False)

		for i in xrange(self.pop.size()):
			tourneyPop.addIndividual( self.pop.individuals[random.randrange(0,self.pop.size())] )

		return tourneyPop.getFittest()