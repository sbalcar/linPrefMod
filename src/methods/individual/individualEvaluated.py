#!/usr/bin/python3

from methods.individual.aIndividual import AIndividual #class


class IndividualEvaluated:
  # individual:AIndividual, fitness:float
  def __init__(self, individual, fitness):
      if not isinstance(individual, AIndividual):
          raise ValueError("Argument individual isn't type AIndividual.")
      if type(fitness) is not float:
          raise ValueError("Argument fitness isn't type float.")
      self.individual = individual
      self.fitness = fitness
  
  def printIndividualEvaluated(self):
      print("IndividualEvaluated fitness: ", self.fitness)


