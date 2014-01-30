from population import Population
from breeder import Breeder

pop = Population()
breed = Breeder(pop)

print pop
print "Avg fitness: " + str(pop.averageFitness())
print "Fittest: " + str(pop.getFittest())

i = 0
while abs(Population.fit.getFitness(pop.getFittest()) - Population.fit.maxFitness()) > .0001:
	i+=1
	pop = breed.evolve()
	print "Generation " + str(i)
	print "Avg fitness: " + str(pop.averageFitness())
	print "Fittest: " + str(pop.getFittest())
	breed = Breeder(pop)
	