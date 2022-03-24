from solution import *
import numpy as numpy
from constants import *
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = dict()
        for x in range(populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID +=1
            
        
        


    def Evolve(self):
        for x in range(self.parents.__len__()):
            self.parents[x].Evaluate("GUI")
        # for currentGeneration in range(numberOfGenerations):
        #     self.Evolve_For_One_Generation()
    
    def Show_Best(self): 
        pass
        # self.parent.Evaluate("GUI")

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        for x in range (self.parents.__len__()):
            self.child = copy.deepcopy(self.parent[x])
            self.child.Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Mutate(self):
        self.child.Mutate()
        print(self.child.fitness)
        print(self.parent.fitness)

    def Select(self):
        if (self.parent.fitness < self.child.fitness):
            self.parent = self.child

    def Print(self):
        #print("parent fitness: " + str(self.parent.fitness) + " child fitness: " + str(self.child.fitness))
        pass



