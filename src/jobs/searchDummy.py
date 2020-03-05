#!/usr/bin/python3

from methods.randomSearch import RandomSearch #class

def search():
    print("RandomSearch")

    # search:RandomSearch
    search = RandomSearch()

    # indiv:float[]
    indiv = search.search(5)

    # fitness:float
    fitness = search.fitness(indiv)

    print(indiv)
    print(fitness)

